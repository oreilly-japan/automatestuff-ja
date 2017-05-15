#! python3
# メール経由で命令をチェックして実行します。
# ここでは、BitTorrentの"magnet"リンクをチェックし、
# Torrentプログラムを実行します。

import smtplib, imapclient, pyzmail, logging, traceback, time, subprocess
from backports import ssl  # gmailに必要

logging.basicConfig(filename='torrentStarterLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 以下の変数を設定してください。
MY_EMAIL = 'my_commander@gmail.com' # このメールからのみ応答する
BOT_EMAIL = 'my_bot@gmail.com'  # ボットのメールアドレス
BOT_EMAIL_PASSWORD = 'my_bot_password'
IMAP_SERVER = 'imap.gmail.com'
SMTP_SERVER = 'imap.gmail.com'
SMTP_PORT = 465
# Torrentのプログラムパス
TORRENT_PROGRAM = 'C:\\Program Files (x86)\\qBittorrent\\qbittorrent.exe'

assert BOT_EMAIL != MY_EMAIL, "ボットのアドレスは別にしてください."


def getInstructionEmails():
    # imapClientでログイン
    logging.debug('Connecting to IMAP server at %s...' % (IMAP_SERVER))
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    imapCli = imapclient.IMAPClient(IMAP_SERVER, ssl=True, ssl_context=context)
    imapCli.login(BOT_EMAIL, BOT_EMAIL_PASSWORD)
    imapCli.select_folder('INBOX')
    logging.debug('Connected.')

    # メールから命令を取得
    instructions = []
    UIDs = imapCli.search(['FROM', MY_EMAIL])
    rawMessages = imapCli.fetch(UIDs, ['BODY[]'])
    for UID in rawMessages.keys():
        # 生のメッセージを解析
        message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])
        if message.html_part != None:
            body = message.html_part.get_payload().decode(message.html_part.charset)
        if message.text_part != None:
            # HTMLとテキストの両方があればテキストの方を用います
            body = message.text_part.get_payload().decode(message.text_part.charset)

        # メール本文から命令を抽出
        instructions.append(body)

    # 受信したメールを削除する。
    if len(UIDs) > 0:
        imapCli.delete_messages(UIDs)
        imapCli.expunge()

    imapCli.logout()

    return instructions


def parseInstructionEmail(instruction):
    # 命令を実行し、応答メールを送ります
    responseBody = 'Subject: Instruction completed.\nInstruction received and completed.\nResponse:\n'

    # メール本文を解析し、命令を取り出します。
    lines = instruction.split('\n')
    for line in lines:
        if line.startswith('magnet:?'):
            # Torrentプログラムを実行
            subprocess.Popen(TORRENT_PROGRAM + ' ' + line) 
            print(TORRENT_PROGRAM + ' ' + line)
            responseBody += 'Downloading magnet link.\n'

    # ボットが命令を実行したことを確認する応答文をメールする
    logging.debug('Connecting to SMTP server at %s to send confirmation email...' % (SMTP_SERVER))

    smtpCli = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 
    smtpCli.ehlo()
    smtpCli.starttls() 
    smtpCli.login(BOT_EMAIL, BOT_EMAIL_PASSWORD)
    logging.debug('Connected.')
    smtpCli.sendmail(BOT_EMAIL, MY_EMAIL, responseBody)
    logging.debug('Confirmation email sent.')
    smtpCli.quit()


# メールをチェックし命令実行する無限ループを開始します。
print('メールボットが始動しました。停止するにはCtrl-Cを押してください。')
logging.debug('Email bot started.')
while True:
    try:
        logging.debug('Getting instructions from email...')
        instructions = getInstructionEmails()
        for instruction in instructions:
            logging.debug('Doing instruction: ' + instruction)
            parseInstructionEmail(instruction)
    except Exception as err:
        logging.error(traceback.format_exc())

    # 15分待って、再度チェックします。
    logging.debug('Done processing instructions. Pausing for 15 minutes.')
    time.sleep(60 * 15)

#! python3
# textmyself.py - 引数の文字列をSMSで送信するtextmyself()関数を定義する

# 設定値
account_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilio_number = '+12345678901' # 購入した米国の電話番号
my_number = '+819012345678'   # 自分の携帯電話番号

try:from twilio.rest import TwilioRestClient
except: from twilio.rest import Client as TwilioRestClient

def textmyself(message):
    twilio_cli = TwilioRestClient(account_SID, auth_token)
    twilio_cli.messages.create(body=message, from_=twilio_number, to=my_number)  # ?

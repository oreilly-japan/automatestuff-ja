import imapclient
from backports import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True, ssl_context=context)
imap_obj.login('your_address@gmail.com', 'YOUR_PASSWORD')

imap_obj.select_folder('INBOX', readonly=True)

UIDs = imap_obj.search('(SINCE 05-Jul-2014)')

print(UIDs)

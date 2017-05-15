import smtplib
from email.header import Header
from email.mime.text import MIMEText

charset = 'iso-2022-jp'

msg = MIMEText('日本語の本文', 'plain', charset)
msg['Subject'] = Header('日本語の件名'.encode(charset), charset)

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login('your_address@gmail.com', 'YOUR_PASSWORD')
smtp_obj.sendmail('your_address@gmail.com', 'to_address@gmail.com', msg.as_string())
smtp_obj.quit()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import random
import string

sender_email = "2747546199@qq.com"
app_password = "rspsauskdnkldgbi"

def generate_verification_code():
    # 生成数字和字母的字符集
    characters = string.digits + string.ascii_letters
    # 生成六位验证码
    verification_code = ''.join(random.choice(characters) for _ in range(6))
    return verification_code

def send_message(receiver_email,Subject,body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = Subject

    msg.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP('smtp.qq.com', 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())








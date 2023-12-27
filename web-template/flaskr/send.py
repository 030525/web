import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



sender_email = "2747546199@qq.com"
app_password = "rspsauskdnkldgbi"



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

def send_verify_code(email,code):
    Subject = "来自科技金融第九组项目:BigDataLending 的验证码"
    body = f"您的验证码是: {code} , 本验证码约60秒的时效 , 请尽快使用 , 祝您生活愉快!"  

    send_message(email,Subject,body)




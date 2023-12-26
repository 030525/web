from send import *


Subject = "来自科技金融第九组项目:BigDataLending 的验证码"
body = f"您的验证码是: {generate_verification_code()} , 祝您生活愉快!"

a = send_message("xwj2003525@qq.com",Subject,body)
print(a)
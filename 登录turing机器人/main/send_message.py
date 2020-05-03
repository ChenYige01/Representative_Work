'''
文件说明 : 发送验证码
编写作者 : Chenyg
编写时间 : 2020年4月5日
'''
import smtplib
from email.mime.text import MIMEText
import easygui as g
import random
import email_address



def send_message(address):
    try:
        yanzhen1 = str(random.randint(10000,99999))
        smtp_server = 'smtp.qq.com'
        user = 'cyg2100218975@qq.com'
        password = 'jnlmsqmpalfzeeba'
        receivers = address

        subject = "Cyg's verification code"
        message = MIMEText(yanzhen1,'html', 'utf-8')
        message['From'] = user
        message['To'] = receivers
        message['subject'] = subject
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server)
        smtp.login(user,password)
        smtp.sendmail(user,receivers,message.as_string())
        smtp.quit()

        yanzhen2 = g.enterbox('Enter the verification code : ')
        a = 1

        while a <=2:
            if yanzhen1 == yanzhen2:
                g.msgbox('Verify success')
                return 1
                break

            else:
                yanzhen2= g.enterbox('Verification failed, please re-enter the verification code')
                return 0
                a += 1

        if a >= 3:
            g.msgbox('Verification failed')
            g.msgbox("See you next time")
            return 0

    except Exception as e:
        new_receivers = g.enterbox("Please enter correct email address : ")
        send_message(new_receivers)

def send_message_run():
    a = email_address.get_email_address()
    send_message(a)

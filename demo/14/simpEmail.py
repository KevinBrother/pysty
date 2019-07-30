# email 构建email
# SMTP 发送邮件

from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP

def main():
    message = MIMEText('出来玩','plain', 'utf-8')
    message['From'] = Header('brother', 'utf-8')
    message['To'] = Header('上天选中的人', 'utf-8')
    message['Subject'] = Header('你要发财了', 'utf-8')

    smtper = SMTP('smtp.qq.com')
    sender = '1301239018@qq.com'
    password = 'azqyskteopwugcaf'
    # receivers = ['1299178488@qq.com', '893875944@qq.com']
    receivers = ['1299178488@qq.com']
    smtper.login(sender, password)
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')

if __name__ == "__main__":
    main()
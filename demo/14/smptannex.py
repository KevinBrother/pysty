from email.header import Header
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def main():
    message = MIMEMultipart()

    text_content = MIMEText('附件中有本月数据', 'plain', 'utf-8')

    message['Subject'] = Header('本月数据', 'utf-8')
    message.attach(text_content)

    with open('/home/brother/桌面/daily', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=daily.txt'
        message.attach(txt)
    
    with open('/home/brother/桌面/addr.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=addr.xlsx'
        message.attach(xls)
    
    smtper = SMTP('smtp.qq.com')
    sender = '1301239018@qq.com'
    password = 'azqyskteopwugcaf'
    # receivers = ['1299178488@qq.com', '893875944@qq.com']
    receivers = ['1299178488@qq.com']
    smtper.login(sender, password)
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('邮件发送完成')

if __name__ == "__main__":
    main()
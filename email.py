# coding:utf-8
# smtplib模块负责连接服务器和发送邮件
# MIMEText：定义邮件的文字数据
# MIMEImage：定义邮件的图片数据
# MIMEMultipart：负责将文字图片音频组装在一起添加附件
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from scripts.constants import const

print(const.SENDER)

sender = const.SENDER
receive = const.RECEIVE
passwd = const.PASSWD
mailserver = const.MAILSERVER
port = const.PORT
sub = const.SUB


try:
    msg = MIMEMultipart('related')
    msg['From'] = formataddr(["sender", sender])  # 发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(["receiver", receive])  # 收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = sub
    #文本信息
    #txt = MIMEText('this is a test mail', 'plain', 'utf-8')
    #msg.attach(txt)

    #附件信息
    # attach = MIMEApplication(open("F:\\git\\TraPlan\\helloworld.txt").read())
    # attach.add_header('Content-Disposition', 'attachment', filename='git_helloworld')
    # msg.attach(attach)

    #正文显示图片
    body = """
    <b>hello ,my baby</b> 
    <br><img src="who is it"><br>
    """
    text = MIMEText(body, 'html', 'utf-8')
    f = open('F:\\beauty.png', 'rb')
    pic = MIMEImage(f.read())
    f.close()
    pic.add_header('Content-ID', '<image>')
    msg.attach(text)
    msg.attach(pic)


    server = smtplib.SMTP(mailserver, port)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(sender, passwd)  # 发件人邮箱账号、邮箱密码
    server.sendmail(sender, receive, msg.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()
    print('success')
except Exception as e:
    print(e)
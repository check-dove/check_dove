import smtplib, time
# 用Message来构建消息，并设置其属性，用set_playload方法设置邮件内容
# 故这里没用MIMEtext模块进行消息内容设置
from email.message import Message, MIMEPart
from time import sleep
import email.utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
"""
    两种的连接、发送比较研究一下
"""

smtpserver = 'smtp.qq.com'
username = '2684164326@qq.com'
password = 'zgezpaylitmvecih'

fromaddr = '2684164326@qq.com'
toaddr = '766929305@qq.com'
msgs = {'subject': '这是测试', 'content': '测试'}

times = email.utils.formatdate(time.time(), True)


def sendmails(fromaddr, toaddr, msgs):
    """
        只用Message构建消息
    :param fromaddr:
    :param toaddr:
    :param msgs:
    :return:
    """
    message = Message()
    message['Subject'] = msgs['subject']
    message['From'] = fromaddr
    message['To'] = toaddr
    message.set_payload(msgs['content'] + '\n' + times)
    m = message.as_string()

    sm = smtplib.SMTP(smtpserver, port=587, timeout=20)
    sm.ehlo()
    sm.starttls()
    sm.ehlo()
    sm.login(username, password)
    sleep(2)
    sm.sendmail(fromaddr, toaddr, m.encode('utf8'))
    sleep(2)
    sm.quit()
    return True


def sendmail_mime(fromaddr, toaddr, msgs):
    """
        使用MIMEMultipart构建消息，并添加附件进行发送
    :param fromaddr:
    :param toaddr:
    :return:
    """
    with open('a.txt', 'rb+') as f:
        content = f.read()

    # 添加正文
    message = MIMEPart()
    message.set_content(msgs['content'] + '\n' + times)

    # 添加附件
    # 通过MIMEText定义邮件的正文、格式、编码；
    # Content-Type指定附件内容的类型。在这里后面的参数表示二进制流
    # Content-Disposition指定显示附件的文件；在这里后面的参数指定文件名
    att = MIMEText(content, 'text', 'utf-8')
    att['Content_Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="a.txt"'

    # 邮件消息构建，添加主题、发送人、收件人
    msg = MIMEMultipart()
    msg['Subject'] = msgs['subject']
    msg['From'] = fromaddr
    msg['To'] = toaddr

    # 为消息绑定正文内容、和附件
    msg.attach(message)
    msg.attach(att)

    # 创建邮件服务，登录并发送消息
    sm = smtplib.SMTP()
    sm.connect(smtpserver)
    sm.login(username, password)
    sleep(2)
    sm.sendmail(fromaddr, toaddr, msg.as_string().encode('utf-8'))
    sm.quit()


if __name__ == '__main__':
    sendmail_mime(fromaddr, toaddr, msgs)
    print('done!')

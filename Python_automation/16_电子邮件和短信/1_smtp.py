import configparser
import smtplib

conf = configparser.ConfigParser()
conf.read('/home/ryan/Desktop/code.ini')
code = conf.get('Code', 'code')

# 登录到SMTP服务器
smtp_obj = smtplib.SMTP('smtp.163.com')
smtp_obj.login('a844020228@163.com', code)
print(smtp_obj.ehlo())

# 发送邮件
# sendmail(发件人, 收件人, 邮件内容)，邮件内容是一个字符串，以 Subject: 开头。返回的是字典，如果发送失败，
# 对于发送失败的收件人会生成一个键值对在字典中
smtp_obj.sendmail('a844020228@163.com', 'a844020228@163.com', 'Subject: test\n\nHello, this is a test email.')
smtp_obj.quit()
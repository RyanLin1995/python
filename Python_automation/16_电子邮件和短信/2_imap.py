import configparser

import imaplib

conf = configparser.ConfigParser()
conf.read('/home/ryan/Desktop/code.ini')
code = conf.get('Code', 'code')

imaplib.Commands['ID'] = ('AUTH')

conn = imaplib.IMAP4_SSL(port=993, host='imap.163.com')
conn.login('a844020228@163.com', code)

# 上传客户端身份信息
args = ("name", "Ryan", "contact", "a844020228@163.com", "version", "1.0.0", "vendor", "myclient")
typ, dat = conn._simple_command('ID', '("' + '" "'.join(args) + '")')

status, uid = conn.select('&XfJT0ZAB-', readonly=True)
sent_items_status,  sent_items_status_raw_data = conn.fetch(uid[0].decode(), '(RFC822)')
print(sent_items_status_raw_data)


# with IMAPClient('imap.163.com') as client:
#     client.login('a844020228@163.com', code)
#     print(client.list_folders())
#     client.select_folder('已发送', readonly=True)
#     uids = client.search(['ALL'])
#     raw_messages = client.fetch(uids, ['BODY[]', 'FLAGS'])  # search() 参数 readonly=True 时，使用 fetch() 不会将邮件标为已读，
#     # readonly=False 时，使用 fetch() 则会将邮件标为已读


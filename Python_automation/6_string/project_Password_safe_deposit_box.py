import sys
import pyperclip

PASSWORD = {'email': '123456789',
            'qq': '987654321',
            'blog': '12345'}

print(sys.argv)

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print("Password for {} copied to clipboard".format(account))

else:
    print("No such account: {}".format(account))
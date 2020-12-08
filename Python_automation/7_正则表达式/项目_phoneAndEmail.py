import re
import pyperclip

# match the phone number
phoneRegex = re.compile(r"""((\d{3}|\(\d{3}\))?  # area code 
                        (\s|-|.)?  # separator
                        (\d{3})  # first3 digits
                        (\s|-|.)?  # separator
                        (\d{4})  # last 4 digits
                        (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
                        )""", re.VERBOSE)

# match the mail address
mailRegex = re.compile(r"""([a-zA-Z0-9._%+-]+  # username
                       @  # @ symbol
                       [a-zA-Z0-9]+  # domain name
                       (\.[a-zA-Z0-9]{2,4})  # dot-something
                       (\.[a-zA-Z0-9]{2,4})?  # dot-something
                       )""", re.VERBOSE)

text = str(pyperclip.paste())
matches = []

# find the match in the clipboard text
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])

    if groups[6] != '':
        phoneNum += ' x' + groups[6]
    matches.append(phoneNum)

for groups in mailRegex.findall(text):
    matches.append(groups[0])

# copy result to clipboard
if len(matches) > 0:
    ret = '\n'.join(matches)
    pyperclip.copy(ret)
    print('Copied to clipboard:')
    print(ret)

else:
    print('No anything found')
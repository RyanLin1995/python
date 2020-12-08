import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = "* {}".format(lines[i])

text = "\n".join(lines)

pyperclip.copy(text)
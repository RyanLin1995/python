import re

# . 可以匹配除换行之外的字符， .* 可以匹配任意多个非换行的字符
# 但如果在 re.compile 中加上re.DOTALL 或在 re.match 中加入 re.S，可以匹配出换行符

# re.compile 中不入 re.DOTALL
noNewLineRegex = re.compile(r'.*')
ret = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(ret.group())

# re.compile 中加入 re.DOTALL
newLineRegex = re.compile(r'.*', re.DOTALL)
ret = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(ret.group())

# re.match 中不加 re.S
noNewLineRegex = re.match(r'.*', 'Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(noNewLineRegex.group())

# re.match 中加入 re.S
newLineRegex = re.match(r'.*', 'Serve the public trust.\nProtect the innocent.\nUphold the law.', re.S)
print(newLineRegex.group())
import re

# 读取文本
file = open('/home/ryan/python/Python_automation/8_读写文件/疯狂填词/madlibs.txt', 'r')
words = file.read()
file.close()
# 查找关键字
pattern = re.compile('ADJECTIVE|NOUN|VERB|ADVERB', re.I)
mo = pattern.findall(words)
# 依次替换每一个关键字
for word in mo:
    repl = input(f'Enter a {word}:\n> ')
    regex = re.compile(word)
    words = regex.sub(repl, words, 1)

print(words)
# 替换后的文本写入新的文件
new_file = open('~/python/Python_automation/8_读写文件/疯狂填词/madlibs.txt', 'w')
new_file.write(words)
new_file.close()

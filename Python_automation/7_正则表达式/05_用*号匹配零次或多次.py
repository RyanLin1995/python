import re

batRegex = re.compile(r'Bat(wo)*man')

# 匹配零次
mo1 = batRegex.search("The Adventures of Batman")
print(mo1.group())

# 匹配一次
mo2 = batRegex.search("The Adventures of Batwoman")
print(mo2.group())

# 匹配多次
mo3 = batRegex.search("The Adventures of Batwowowowowowoman")
print(mo3.group())

# *号表示匹配零次或多次

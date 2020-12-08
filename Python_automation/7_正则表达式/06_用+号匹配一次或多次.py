import re

batRegex = re.compile(r'Bat(wo)+man')

# 匹配一次
mo1 = batRegex.search("The Adventures of Batwoman")
print(mo1.group())

# 匹配多次
mo2 = batRegex.search("The Adventures of Batwowowowowowoman")
print(mo2.group())

# 无法匹配，因为+号不是可选项
mo3 = batRegex.search("The Adventures of Batman")
print(mo3 is None)

# +号表示匹配一次或多次，如果没有则不匹配

# 例子:
numRegex = re.compile(r'(\d)+')
num = numRegex.search("19")
print(num.group())

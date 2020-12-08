import re

# 在正则表达式中添加括号，将创建分组
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search("My phone number is 444-525-8017")

# 创建分组后，调用 group 方法或传入 group(0) 将打印将打印全部匹配的文本
print(mo.group())

# 向 group 传入数字，将打印对应的分组，如 group(1) 将打印分组1，group(2) 将打印分组2
print(mo.group(1))
print(mo.group(2))

# 如果想打印整个分组，可以调用 Regex 对象的 groups 方法
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

print()
# 因为()在正则表达式中有特殊含义，如果需要匹配括号，需要转义
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search("My phone number is (444) 525-8017")

print(mo.group(1))
print(mo.group(2))
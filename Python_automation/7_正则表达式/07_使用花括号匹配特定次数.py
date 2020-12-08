import re

haRegex = re.compile(r'(haha){,3}')
mo1 = haRegex.search("hahahahaha")
print(mo1.group())

mo2 = haRegex.search("hahaha")
print(mo2.group())

mo3 = haRegex.search("ha")
print(mo3.group())


numRegex = re.compile(r'(\d){0,5}')
num1 = numRegex.search('1')
print(num1.group())

# {}表示匹配特定次数。
# {}里面只有一个整数，表示匹配该字符的次数，如(a){5}: 表示匹配 a 字符5次，即匹配 aaaaa
# {}里面有两个整数加一个逗号(,)，表示匹配一个范围，如(a){3,5}: 表示匹配 a 字符3-5次,即匹配aaa|aaaa|aaaaa
# {}里面如果只有一个整数和一个逗号(,)，表示匹配一个范围的缩写，如(a){,5}: 表示匹配 a 字符0-5次，即匹配|a|aa|aaa|aaaa|aaaaa;
# (a){5,}: 表示匹配 a 字符5-无限次，即匹配aaaaa|aaaaaa|...
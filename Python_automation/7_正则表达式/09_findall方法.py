import re

# 使用 search 方法，只返回第一个匹配的文本
phoneRegex = re.compile(r'(\d){3}-(\d){4}-(\d){4}')
mo1 = phoneRegex.search('Cell: 411-5555-2309 Work: 212-5146-4156')
print("mo1:", mo1.group())

# 使用 findall 方法，正则表达式没有分组，将会返回一个列表，列表的每个表项为匹配的文本
phoneRegex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
mo2 = phoneRegex.findall('Cell: 411-5555-2309 Work: 212-5146-4156')
print("mo2:", mo2)

# 使用 findall 方法，正则表达式有分组，将返回一个列表，列表的每个表项为元祖，元祖的值为匹配组的字符串
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
mo3 = phoneRegex.findall('Cell: 411-5555-2309 Work: 212-5146-4156')
print("mo3: ", mo3)

# findall()返回的结果如下：
# 1. 如果被调用在一个没有分组的正则表达式上，返回的是列表，列表的值为匹配的文本
# 2. 如果被调用在一个含有分组的正则表达式上，返回的也是列表，但是列表的值为元祖，元祖的值为匹配分组的字符串
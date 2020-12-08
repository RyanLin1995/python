import re

# 插入符号 ^ 表示匹配必须发生在被查找文本的开始处
# 美元符号 $ 表示匹配必须以这个正则表达式的模式结束
# 同时使用 ^ 与 $ 表示整个字符串必须匹配该正则表达式

# 1. 匹配以 Hello 开头的字符串
beginsWithHello = re.compile(r'^Hello')
ret1 = beginsWithHello.search('Hello World')
print(ret1.group())

ret2 = beginsWithHello.search('He say Hello')
print(ret2 is None)

# 2. 匹配数字0到9结尾的字符串
endsWithNumber = re.compile(r'\d$')
ret3 = endsWithNumber.search('Your number is 42')
print(ret3.group())

ret4 = endsWithNumber.search('Your number is two')
print(ret4 is None)

# 3. 匹配开始到结束都是数字的字符串
wholeStringIsNumber = re.compile(r'^\d+$')
print(wholeStringIsNumber.search('123456789').group())
print(wholeStringIsNumber.search('123abc456xyz789') is None)
print(wholeStringIsNumber.search('1 234 5678 9') is None)

import re

# 编写一个正则表达式，匹配每3位数就有有一个逗号的数字。
# 如:
# 42
# 1,234
# 6,368,745
# 但是不匹配以下:
# 12,34,567(逗号间只有两个数字)
# 1234(没有逗号)

numRegex = re.compile(r'(\d{1,3})(\.?)(\d{3})?\2?(\d{3})?')
ret = numRegex.match('123.456.789')
print(ret.group())


# 编写一个正则表达式，匹配姓名为 Nakamoto 的完整名字
# 如匹配: Satoshi Nakamoto,Alice Nakamoto,RoboCop Nakamoto
# 不匹配: Nakamoto(没有名字),roboCop Nakamoto(名字没大写),RoboCop nakamoto(姓名没大写)
nameRegex = re.compile(r'([A-Z]\w*\s)+[A-Z]\w*')
ret = nameRegex.match('RoboCop Nakamoto')
print(ret.group())


# 编写一个正则表达式，匹配第一个词为Alice、Bob或Carol，第二个词为eats、pets或throws，第三个词为apples、cats或baseball，最后以 。 结束，且不区分大小写
contentRegex = re.compile(r'(alice|bob|carol)\s+(eats|pets|throws)\s+(apples|cats|baseball).', re.I)
ret = contentRegex.search('BOB EATS APPLES.')
print(ret.group())
import re

# 1. 用 \d 匹配单个数字，\d 只能匹配数字 0-9
ret1 = re.match(r'速度与激情\d', '速度与激情8')
print(ret1.group())

print(re.match(r'速度与激情\d', '速度与激情10').group())

# 2. 用 [] 匹配单个连续数字或字符
ret2 = re.match(r'速度与激情[123456789]', '速度与激情9')
print(ret2.group())

# print(re.match(r'速度与激情[12345678]', '速度与激情9').group())

# 3. 用 [] 匹配单个不连续的数字或字符
ret3 = re.match(r'速度与激情[1-36-9]', '速度与激情3')
print(ret3.group())

print(re.match(r'速度与激情[1-36-9]', '速度与激情5').group())
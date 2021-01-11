import re

# 1. 使用 {} 匹配多个字符
# 其中 {n} 表示匹配前一个字符 n 次
# {m, n} 表示匹配前一个字符 m 到 n 次
ret1 = re.match(r'速度与激情\d{3}', '速度与激情123')
print(ret1.group())

ret2 = re.match(r'速度与激情\d{1,3}', '速度与激情23')
print(ret2.group())

# 2. 使用 ? 匹配前一个字符的0次或1次，即要么有1次，要么没有
ret3 = re.match(r'\d{3,4}-?\d{7,8}', '020-22432213')
print(ret3.group())

ret4 = re.match(r'\d{3,4}-?\d{7,8}', '07578163288')
print(ret4.group())

# 3. 使用 * 匹配前一个字符0次或无限次，即可有可无以及使用 re.S 打印换行符\n
content = """this is a test
I don't know what I can input
so I input some words
that's all
Thank you"""

ret5 = re.match(r'.*', content)
print(ret5.group())

ret6 = re.match(r'.*', content, re.S)
print(ret6.group())

# 4. 使用 + 匹配前一个字符1次或无限次，即至少有1次
ret7 = re.match(r'.+', 'abcd')
print(ret7.group())

print(re.match(r'.+', '').group())

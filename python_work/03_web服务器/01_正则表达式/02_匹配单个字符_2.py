import re

# 1. 匹配单个数字或字母
ret = re.match(r'速度与激情[1-8a-zA-Z]', "速度与激情q")
print(ret.group())

print(re.match(r'速度与激情[1-8a-zA-Z]', '速度与激情Q').group())

# 2. 使用 \w 匹配单词字符，即匹配a-z，A-Z，0-9，_
# PS: \W 匹配的是非单词字符
print(re.match(r'速度与激情\w', '速度与激情9').group())
print(re.match(r'速度与激情\w', '速度与激情G').group())
print(re.match(r'速度与激情\w', '速度与激情_').group())
print(re.match(r'速度与激情\w', '速度与激情二').group())

# 3. 使用 \s 匹配空白字符，即空格，tab键
print(re.match(r'速度与激情\s\d', '速度与激情 9').group())
print(re.match(r'速度与激情\s\d', '速度与激情\t9').group())  # \t 代表 tab键

# 4. 使用 . 匹配任意一个字符，除了 \n
print(re.match(r'速度与激情.', '速度与激情%').group())
print(re.match(r'速度与激情..', '速度与激情 9').group())
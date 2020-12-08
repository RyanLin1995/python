import re

# 正则表达式步骤
# 1. import re
# 2. 用re.compile创建一个Regex对象，其中compile里面传入正则表达式
# 3. 调用Regex对象的search方法，search里面传入被查找对象
phonenumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # 添加r使字符串变为原始字符串，即不用转义

mo = phonenumRegex.search("My phone number is 444-525-8017")

print(mo.group())
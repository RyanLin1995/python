import re

# 可以用 [] 建立自己的字符分类
# 如果在左方括号后方加上^，表示非字符类

# 1. 创建元音字符的字符分类
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

# 2. 创建非元音字符的字符分类
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo2 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo2)

# 在 [] 中使用 ., *, ? 或 () 等普通的正则表达式字符并不需要转义。如匹配0到5加一个句号为[0-5.] 而不是[0-5\.]
# 在 [] 中可以使用 - 表示一个范围的匹配。如匹配123456789为[1-9]

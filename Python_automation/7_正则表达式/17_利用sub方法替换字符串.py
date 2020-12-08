import re

# 利用 sub 方法可以替换符合正则表达式的字符
nameRegex = re.compile(r'Agent \w+')
ret = nameRegex.sub('CENSORED', 'Agent Alice gave the secret document to Agent Bob')
print(ret)

# 在 sub 方法中，如果正则表达式有分组()，可以利用 \1, \2, \3表示不同的分组
# 例如，想要只显示用户名的第一个字母
agentnameRegex = re.compile(r'Agent\s(\w)\w*')  # 指匹配了Agent 后面的姓名，并保留姓名的第一个字符
# ret = agentnameRegex.sub(r'Agent \1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
ret = agentnameRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(ret)

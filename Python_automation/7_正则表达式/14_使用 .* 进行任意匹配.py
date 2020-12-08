import re

# . 代表除了换行 \n 意外的任意字符
# * 代表前一个字符的零次或多次
# .* 代表匹配所有除换行 \n 之外的所有字符
nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
ret = nameRegex.search("First name: Ryan Last name: Lin")
print(ret.group(1))
print(ret.group(2))

# .* 匹配为贪心匹配，可以在 .*? 进行非贪心匹配

# 案例: 匹配左边一个尖括号，中间任意字符，右边一个尖括号
# 非贪心匹配，匹配最短结果
nongreddyRegex = re.compile(r'<.*?>')
ret = nongreddyRegex.search("<To serve man> for dinner.>")
print(ret.group())

# 贪心匹配，匹配最长结果
greddyRegex = re.compile(r'<.*>')
ret = greddyRegex.search("<To serve man> for dinner.>")
print(ret.group())
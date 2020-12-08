import re

# python的正则表达式默认是贪心匹配，表示在有二义的情况下，默认匹配最长的。
# 可以在大括号后加上 ? ，声明非贪心匹配

# 贪心匹配
greedyHaRegex = re.compile(r'(ha){3,5}')
mo1 = greedyHaRegex.search('hahahahahaha')
print(mo1.group())

# 非贪心匹配
nongreedyHaRegex = re.compile(r'(ha){3,5}?')
mo2 = nongreedyHaRegex.search('hahahahahaha')
print(mo2.group())

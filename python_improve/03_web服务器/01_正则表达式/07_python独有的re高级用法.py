import re

# 1. re.search: 在整个文本中匹配第一个符合正则表达式的字符
# 需求: 匹配出文章的阅读次数

ret = re.search(r'\d+', '阅读次数为: 9999')
print(ret.group())

# 2. re.findall: 匹配出所有符合正则表达式的文本，并把值生成为列表
# 需求: 统计出python，c，c++相应文章的阅读次数

ret = re.findall(r'\d+', 'python = 9999, c = 1357, c++ = 2468')
print(ret)

# 2.1 re.finditer: 匹配出所有符合表达式的非重复文本，返回的是迭代器
all_matchs = re.finditer(r'\d+', 'one1two2three3four4one1two2three3four4')
for match in all_matchs:
    print(match.span())  # span([group])返回一个二元组 (m.start(group), m.end(group)), 注意如果 group 没有在这个匹配中，就返回 (-1, -1) 。group 默认为0，即整个匹配

# 3. re.sub
# re.sub用法一: 将匹配到的结果替换为中间的
ret = re.sub(r'\d+', '996', '上班时间985')
print(ret)


# re.sub用法二: 将匹配到的结果作为参数传入函数
def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r'\d+', add, "上班时间996")
print(ret)

# 4. re.split: 根据正则表达式进行切割字符串并返回列表
# 需求: 切割字符串"info:xiaoZhang 33 shandong"
ret = re.split(r'[: ]', 'info:xiaoZhang 33 shandong')
print(ret)

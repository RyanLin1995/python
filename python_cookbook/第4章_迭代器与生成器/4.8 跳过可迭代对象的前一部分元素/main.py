from itertools import dropwhile

with open('sample.sh') as f_1:
    for line in dropwhile(lambda line: line.startswith('#'), f_1):  # 跳过所有以 # 开头的段落，知道出现第一个不为 # 开头的字段为止
        print(line, end='')

print('\n' + '-' * 50)
# 上下两个代码不同之处在于，下面的代码，是会把所有以 # 开头的段落都去掉
with open('sample.sh') as f_2:
    lines = (line for line in f_2 if not line.startswith('#'))
    for line in lines:
        print(line, end='')

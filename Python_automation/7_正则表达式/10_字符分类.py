import re

xmasRegex = re.compile(r'\d+\s\w+')
ret = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, '
                        '8 maids, 7 swans, 6 geese, 5 rings, 4 birds, '
                        '3 hens, 2 doves, 1 partridge')
print(ret)

# \d : 0到9的任何数字
# \D : 除0到9的数字以外的任何字符
# \w : 任何字母，数字或下划线字符(可以认为匹配单词字符)
# \W : 除字母，数字和下划线以外的任何字符
# \s : 空格，制表符或行符(可以认为匹配空白字符)
# \S : 除空格，制表符和换行符以外的任何字符

import re

# . 为通配符，可以匹配除了换行符 \n 之外的任意任意字符，但是只能匹配1个字符
atRegex = re.compile(r'.at')
ret = atRegex.findall('The cat in the hat sat on the flat mat.')
print(ret)  # 因为 . 只匹配一个字符，因此 flat 只显示 lat 而不显示 flat

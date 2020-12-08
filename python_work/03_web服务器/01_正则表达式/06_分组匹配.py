import re

# 1. 利用()进行分组，且利用 | 管道符匹配多个分组
ret = re.match(r'[a-zA-Z0-9]{4,20}@(163|126)\.com', 'laowang@126.com')
print(ret.group())

print(re.match(r'[a-zA-Z0-9]{4,20}@(163|126)\.com', 'test@163.com').group())

# 2. 在一个正则表达式中有多个分组，并获取分组的数据
ret = re.match(r'([a-zA-Z0-9]{4,20})@(163|126)\.com', 'laowang@126.com')
print(ret.group(0))
print(ret.group(1))
print(ret.group(2))

# 3. 利用数字表示在一个正则表达式中重复利用分组，即第一个()对应\1，第二个()对应\2
html_str = '<h1>hahahahaha</h1>'
ret = re.match(r'<(\w*)>.*<(/\1)>', html_str)
print(ret.group())

html_str = '<body><h1>hahahahaha</h1></body>'
ret = re.match(r'<(\w*)><(\w*)>.*<(/\2)></\1>', html_str)
print(ret.group())

# 4. 利用别名在一个正则表达式中重复利用分组，即用(?P<name>)起分组别名，用(?P=name)读取分组别名
html_str = '<h1>hahahahaha</h1>'
ret = re.match(r'<(?P<p1>\w*)>.*</(?P=p1)>', html_str)
print(ret.group())

html_str = '<body><h1>hahahahaha</h1></body>'
ret = re.match(r'<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>', html_str)
print(ret.group())
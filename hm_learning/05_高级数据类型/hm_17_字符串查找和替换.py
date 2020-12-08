hello_str = "hello world"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("h"))

# 2. 判断是否以指定字符串结束
print(hello_str.endswith("d"))

# 3. 查找指定字符串
# index同样可以查找指定字符串的索引
# 但是如果指定字符串不存在,index会报错,find会返回-1
print(hello_str.find("l"))
print(hello_str.index("l"))

# 4. 替换字符串
# replace会生成一个新的字符串,不会影响原来的字符串
print(hello_str.replace("world", "python"))
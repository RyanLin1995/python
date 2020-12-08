name_list = ['zhangsan', 'lisi', 'wangwu']

# del可以从内存中删除指定变量，删除后后续的代码不能再使用变量
# 日常开发中，建议使用列表提供的方法代替del

del name_list[1]

print(name_list)
# 介绍：zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# zip() 基本语法：zip([iterable, ...])
# iterable：可迭代对象或迭代器
# 返回值：返回一个可迭代对象

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9, 10]

# 1. zip 简单演示
print(zip())  # 返回的是一个对象
print(list(zip(a, b)))  # 把 a 列表中的每个数值与 b 列表中的每个数值结合成一个元组
print(list(zip(a, c)))  # 当两个参数长度不一致时，元素个数与最短列表一致

# 2. zip 与 dict 的作用
print(dict(zip(a, b)))  # 可将两个列表的值组成为一个新的字典

# 3. zip的特殊用法
new_data = zip(a, b)
print(new_data)
a1, b1 = zip(*new_data)  # zip(*)与zip()相反，可以理解为解压，返回二维矩阵式
print(a1)
print(b1)


# 介绍：map 函数为 Python 内置函数，是根据指定函数对指定序列做映射
# map() 函数基本语法: map(function, iterable, ...)
# function：函数, iterable：一个或多个序列
# 返回值：返回的是一个迭代器,注意返回的结果只能迭代一次，如果需要多次使用请提前保存结果并处理

a = [1, 2, 3, 4, 5, 6, 7, 8]

# 1. map 简单示例
print(list(map(str, a)))  # 因为 map 的返回值是迭代器，是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list


# 2. map 与函数结合
def square(s):
    return s ** 2


print(list(map(square, a)))


# 3. map 案例
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
name = ['adam', 'LISA', 'barT']


def normalize(name):  # 如果是用于 map 函数，这里的 name 其实不是整个 name 列表，而是每个 name 列表中的值
    return name.lower().title()


print(list(map(normalize, name)))

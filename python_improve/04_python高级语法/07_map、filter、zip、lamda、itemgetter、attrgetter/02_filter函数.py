# 介绍：filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该函数接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# filter() 基本语法: filter(function, iterable)
# function： 判断函数，iterable：可迭代对象。
# 返回值：返回的是一个迭代器,注意返回的结果只能迭代一次，如果需要多次使用请提前保存结果并处理

a = [1, 2, 3, 4, 5, 6, 7, 8, "abc"]


# 1. filter 简单示例
def is_int(n):
    return isinstance(n, int)


print(list(filter(is_int, a)))


# 2. filter 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    b = str(n)
    return b == b[::-1]  # 判断 n 取反值后是否与原来相同


print(list(filter(is_palindrome, range(1, 1000))))

# 3. filter 的一个小应用
a = 'hello----world'
filter(None, a.split("-"))  # 传入 None 时会返回第二个参数（可迭代对象）中非空的值

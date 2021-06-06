# 字典是一个无序的数字集合(在python3.6后字典是有序的)，使用print函数输出字典时，
# 通常的顺序和定义的顺序是不一致的
xiaoming = {"gl_name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75,
            "weight": 75.5}

print(xiaoming)

# 另一种创建字典的方法: dict
# dict(**kwarg)
# dict(mapping, **kwarg)
# dict(iterable, **kwarg)
# 返回的是一个字典
# print(help(dict))

# 实例展示
print(dict())  # 创建了一个空字典
print(dict(a='a', b='b', c='c'))
print(dict(zip(["a", "b", "c", "d"], [1, 2, 3, 4])))  # 映射函数的方式来构造字典
print(dict([('one', 1), ('two', 2), ('three', 3)]))  # 可迭代对象方式构造字典

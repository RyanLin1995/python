# 1. 使用双星号** 实现字典合并
# d1 = {"name": "zhangsan", "age": 27}
# d2 = {"name": "lisi", "age": 28}
d1 = {"age": 27}
d2 = {"name": "lisi"}
d3 = {**d1, **d2}
d4 = d1 | d2  # python 3.9 之后可以使用
print(d3)
print(d4)

print("*" * 50)

# 2. 使用单星号*解包任何可迭代对象
print([1, 2, *range(3)])
l1 = [1, 2]
l2 = [3, 4]
print([*l1, *l2])
print(l1 + l2)

print("*" * 50)

# 3. 使用有序字典去重
from collections import OrderedDict

nums = [10, 2, 3, 21, 10, 3]
print(list(OrderedDict.fromkeys(nums).keys()))  # 去重且保留了顺序

print("*" * 50)


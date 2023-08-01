from functools import partial
from operator import mul

# partial 可以根据提供的可调用对象产生一个新的可调用对象，为原可调用对象的某些参数绑定预定的值
triple = partial(mul, 3)  # 第一个参数是可调用对象，后面跟着任意个要绑定的位置参数和关键字参数

print(triple(7))
print(list(map(triple, range(1, 10))))

# 无论深拷贝还是浅拷贝，都会占用一定的内存空间，只是内存中的值不一样
# 深拷贝: 如果是拷贝的对象为可变类型或拷贝对象为不可变类型，但是其值为可变类型，把拷贝对象的父对象和子对象完整拷贝
# 如果拷贝对象为不可变类型，只会作 指向
# 浅拷贝: 只拷贝对象的父对象，对于子对象，会依旧指向父对象原来的；但是如果拷贝对象为不可变类型，则为指向

import copy

a = [11, 22]
b = [33, 44]
c = [a, b]
d = copy.copy(c)  # 浅拷贝
e = copy.deepcopy(c)  # 深拷贝

print(id(c))
print(id(d))
print(id(e))

# 如果此时对 c 添加数值，那么 d 与 e 都不会添加
c.append([55, 66])
print(c)
print(d)  # d 只共享拷贝前的，而拷贝后再新增的，不会共享
print(e)  # e 为深拷贝，是把整个 c 的父对象和子对象全部复制一份

print('-------------------------')

# 但是使用 copy.copy 或 copy.deepcopy 去拷贝元组等不可变类型(
# 因为不可变类型数据不能更改)时，如果元组中的值为不可变类型，会变为 指向 而不是 拷贝
a = (11, 22)
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))

print('-------------------------')

# 如果元组等不可变类型中的值为可变类型，那么进行 copy.deepcopy 时，会变为深拷贝
a = [11, 22]
b = [33, 44]
c = (a, b)
d = copy.copy(c)
e = copy.deepcopy(c)

print(id(c))
print(id(d))
print(id(e))

a.append(55)
print(c)
print(d)
print(e)

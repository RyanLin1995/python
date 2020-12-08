import copy

# Python 所有的赋值语句都是引用，即当一个变量=xxxxxx时，约定为这个变量指向了xxxxxx
a = [11, 22]  # 仅代表把 a 指向了一块内存，内存中含有一个数值为11,22的列表
b = a  # 代表把 b 指向了一个跟 a 的指向一样的内存，可以理解为最简单的浅拷贝
# 证明:
print(id(a))
print(id(b))

# 深拷贝: copy.deepcopy
# 利用 copy.deepcopy 进行深拷贝，发现 a 与 c 数值相同，但是内存不同
c = copy.deepcopy(a)
print(a)
print(c)
print(id(a))
print(id(c))

# 对 a 列表进行数值的添加，发现 a 列表有改动，c 列表没有，是因为内存完整的拷贝了一份 a 的数据，然后 c 指向了这一份新的内存， 因此 c
# 是深拷贝
a.append(33)
print(a)
print(c)

# 或新建一个列表 d，使列表的值为[a,b]，利用 copy.deepcopy() 进行拷贝并使变量 e
# 指向该拷贝，打印两者第一个数值的内存，发现内存不一直
d = [a, b]
e = copy.deepcopy(d)
print(id(d[0]))
print(id(e[0]))

print('-------------------------')

# 浅拷贝: copy.copy
a = [11, 22]
b = [33, 44]
c = [a, b]  # 即列表的0值指向了 a 指向的内存，列表的1值指向了 b 指向的内存
d = c  # 指 d 指向了 c 所指向的内存

# 利用 copy.copy 进行浅拷贝，发现 c 与 e 的内存不一样。通过打印列表 c 与列表 e 的第一个数值的内存，发现数值都指向了 a
# 所指向的内存，即浅拷贝只拷贝对象表层的东西(只拷贝父对象的，不拷贝子对象的)，如复制文件夹时只复制了快捷方式
e = copy.copy(c)
print(id(c))
print(id(e))
print(id(c[0]))
print(id(e[0]))
a.append(55)
print(c)
print(e)
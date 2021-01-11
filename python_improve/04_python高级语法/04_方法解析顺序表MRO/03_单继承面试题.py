# 以下代码会出现什么
class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)  # 这里因为 Child1.x 之前已经定义为 2， 所以不会再去继承
# Parent.x

# 继承不是复制，而是根据MRO，自己有就用自己的，没有就根据MRO去查找

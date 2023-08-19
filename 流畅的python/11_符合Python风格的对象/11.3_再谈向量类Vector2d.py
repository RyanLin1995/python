from array import array
import math


class Vector2d:
    typecode = 'd'  # 类属性，在实例和字节序列之间转换时使用

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):  # 将 Vector2d 实例变成可迭代对象，这样才能拆包
        return (i for i in (self.x, self.y))  # 也可以写成 yield self.x; yield self.y

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name,
                                       *self)  # 使用 {!r} 获取各个分量的表示形式，然后插值，构成一个字符串。因为 Vector2d 实例是可迭代对象，所以 *self 会把 x 分量和 y 分量提供给 format 方法

    def __str__(self):
        return str(tuple(self))  # 由于 Vector2d 是可迭代对象，因此可以获取一个元组

    def __bytes__(self):
        return ((bytes([ord(self.typecode)])) +  # 先将 typecode 转换成字节序列
                bytes(array(self.typecode, self)))  # 再迭代 Vector2d 实例得到一个数组，将数组转换成字节序列

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


v1 = Vector2d(3, 4)
print(bytes(v1))
print(v1.x, v1.y)

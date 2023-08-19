from array import array
import math


class Vector2d:
    typecode = 'd'  # 类属性，在实例和字节序列之间转换时使用

    def __init__(self, x, y):
        self.__x = float(x)  # 将属性标记为私有属性
        self.__y = float(y)

    @property  # 将读值方法标记为特性
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return ((bytes([ord(self.typecode)])) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec=''):
        components = (format(c, format_spec) for c in self)
        return '({}, {})'.format(*components)

    def __hash__(self):  # 定义 hash 属性
        return hash((self.x, self.y))


v1 = Vector2d(3, 4)
print(hash(v1))

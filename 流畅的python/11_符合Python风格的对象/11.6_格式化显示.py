from array import array
import math


class Vector2d:
    typecode = 'd'  # 类属性，在实例和字节序列之间转换时使用

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

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
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec=''):
        components = (format(c, format_spec) for c in self)  # 使用内置函数 format 将 format_spec 应用到向量的各个分量上，构建一个可迭代格式化字符串
        return '({}, {})'.format(*components)


v1 = Vector2d(3, 4)
print(format(v1))
print(format(v1, '.2f'))

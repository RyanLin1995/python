from array import array
import math


class Vector2d:
    __match_args__ = ('x', 'y')  # 添加类属性。按照位置模式匹配中的顺序列出实例属性
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
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

    def __hash__(self):
        return hash((self.x, self.y))


def positional_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(0, 0):
            print(f'{v!r} is null')
        case Vector2d(0):
            print(f'[v!r] is vertical')
        case Vector2d(_, ):
            print(f'{v!r} is horizontal')
        case Vector2d(x, y) if x == y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')


positional_pattern_demo(1)

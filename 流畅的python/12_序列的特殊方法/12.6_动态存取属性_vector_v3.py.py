from array import array
import reprlib
import math
import operator


class Vector:
    """
    A multi-dimensional ``Vector`` class, take 3

    A ``Vector`` is built from an iterable of numbers::

        >>> Vector([3.1, 4.2])
        Vector([3.1, 4.2])
        >>> Vector((3, 4, 5))
        Vector([3.0, 4.0, 5.0])
        >>> Vector(range(10))
        Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])

    Tests of dynamic attribute access::

        >>> v7 = Vector(range(10))
        >>> v7.x
        0.0
        >>> v7.y, v7.z, v7.t
        (1.0, 2.0, 3.0)


    Dynamic attribute lookup failures::

        >>> v7.k
        Traceback (most recent call last):
          ...
        AttributeError: 'Vector' object has no attribute 'k'
        >>> v3 = Vector(range(3))
        >>> v3.t
        Traceback (most recent call last):
          ...
        AttributeError: 'Vector' object has no attribute 't'
        >>> v3.spam
        Traceback (most recent call last):
          ...
        AttributeError: 'Vector' object has no attribute 'spam'


    Tests of preventing attributes from 'a' to 'z'::

        >>> v1.x = 7
        Traceback (most recent call last):
          ...
        AttributeError: readonly attribute 'x'
        >>> v1.w = 7
        Traceback (most recent call last):
          ...
        AttributeError: can't set attributes 'a' to 'z' in 'Vector'

    Other attributes can be set::

        >>> v1.X = 'albatross'
        >>> v1.X
        'albatross'
        >>> v1.ni = 'Ni!'
        >>> v1.ni
        'Ni!'

    """
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]

    # tag::VECTOR_V3_GETATTR[]
    __match_args__ = ('x', 'y', 'z', 't')  # 让 __getattr__ 实现的动态属性支持位置模式匹配

    def __getattr__(self, name):
        cls = type(self)  # 获取 Vector 类
        try:
            pos = cls.__match_args__.index(name)  # 尝试查询 name 在 __match_args__ 中的位置
        except ValueError:  # 如果未找到则抛出 ValueError，且把 pos 设置为 -1
            pos = -1
        if 0 <= pos < len(self._components):  # 如果 pos 在范围内，则返回对应数值
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'  # 如不在，则抛出异常
        raise AttributeError(msg)

    # end::VECTOR_V3_GETATTR[]

    # tag::VECTOR_V3_SETATTR[]
    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:  # 当 name 字符等于 1 时进入判断
            if name in cls.__match_args__:  # 如果 name 在 __match_args__ 中则设置特殊错误消息
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():  # 同理，如果 name 是小写字母也设置特殊错误消息
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''  # 否则不设置错误消息
            if error:  # 如果存在错误消息则报错
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)  # 对于非单个字符，直接设置

    # end::VECTOR_V3_SETATTR[]

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vector(range(9))
    print(v1.x)
    v1.name = 10
    print(v1.name)

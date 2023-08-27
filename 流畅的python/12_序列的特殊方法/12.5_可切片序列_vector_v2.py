from array import array
import reprlib
import math
import operator


class Vector:
    """
    A multi-dimensional ``Vector`` class, take 2

    A ``Vector`` is built from an iterable of numbers::

        >>> Vector([3.1, 4.2])
        Vector([3.1, 4.2])
        >>> Vector((3, 4, 5))
        Vector([3.0, 4.0, 5.0])
        >>> Vector(range(10))
        Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])

    Test of slicing::

        >>> v7 = Vector(range(7))
        >>> v7[-1]  # <1>
        6.0
        >>> v7[1:4]  # <2>
        Vector([1.0, 2.0, 3.0])
        >>> v7[-1:]  # <3>
        Vector([6.0])
        >>> v7[1,2]  # <4>
        Traceback (most recent call last):
          ...
        TypeError: 'tuple' object cannot be interpreted as an integer
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

    # tag::VECTOR_V2[]
    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):  # 如果 key 参数的值是一个 slice 对象
            cls = type(self)  # 则获取实例得到类
            return cls(self._components[key])  # 然后调用类的构造函数构建一个新的实例
        index = operator.index(key)  # 返回 key 转换为整数的结果
        return self._components[index]  # 如果 key 是单个索引，则转换为整数然后返回 _components 中相应的元素

    # end::VECTOR_V2[]
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v7 = Vector(range(7))
    print(v7[-1])
    print(v7[1:4])
    print(v7[-1:])

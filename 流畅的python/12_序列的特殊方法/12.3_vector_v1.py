from array import array
import reprlib
import math


class Vector:
    """
    A multi-dimensional ``Vector`` class, take 1

    A ``Vector`` is built from an iterable of numbers::

        >>> Vector([3.1, 4.2])
        Vector([3.1, 4.2])
        >>> Vector((3, 4, 5))
        Vector([3.0, 4.0, 5.0])
        >>> Vector(range(10))
        Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])


    Tests with 2-dimensions (same results as ``vector2d_v1.py``)::

        >>> v1 = Vector([3, 4])
        >>> x, y = v1
        >>> x, y
        (3.0, 4.0)
        >>> v1
        Vector([3.0, 4.0])
        >>> v1_clone = eval(repr(v1))
        >>> v1 == v1_clone
        True
        >>> print(v1)
        (3.0, 4.0)
        >>> octets = bytes(v1)
        >>> octets
        b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
        >>> abs(v1)
        5.0
        >>> bool(v1), bool(Vector([0, 0]))
        (True, False)


    Test of ``.frombytes()`` class method:

        >>> v1_clone = Vector.frombytes(bytes(v1))
        >>> v1_clone
        Vector([3.0, 4.0])
        >>> v1 == v1_clone
        True


    Tests with 3-dimensions::

        >>> v1 = Vector([3, 4, 5])
        >>> x, y, z = v1
        >>> x, y, z
        (3.0, 4.0, 5.0)
        >>> v1
        Vector([3.0, 4.0, 5.0])
        >>> v1_clone = eval(repr(v1))
        >>> v1 == v1_clone
        True
        >>> print(v1)
        (3.0, 4.0, 5.0)
        >>> abs(v1)  # doctest:+ELLIPSIS
        7.071067811...
        >>> bool(v1), bool(Vector([0, 0, 0]))
        (True, False)


    Tests with many dimensions::

        >>> v7 = Vector(range(7))
        >>> v7
        Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])
        >>> abs(v7)  # doctest:+ELLIPSIS
        9.53939201...


    Test of ``.__bytes__`` and ``.frombytes()`` methods::

        >>> v1 = Vector([3, 4, 5])
        >>> v1_clone = Vector.frombytes(bytes(v1))
        >>> v1_clone
        Vector([3.0, 4.0, 5.0])
        >>> v1 == v1_clone
        True


    """
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)  # 实例属性，保存在一个数组中

    def __iter__(self):
        return iter(self._components)  # 构建一个迭代器用于迭代

    def __repr__(self):
        components = reprlib.repr(self._components)  # reprlib.repr 用于生成有限长度的表示形式
        components = components[components.find('['):-1]  # 去掉 array('d',和后面的)
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))  # 直接使用 self._components 构建 bytes 对象

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(*self)  # Python3.8开始 math.hypot接受N维坐标点

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vector([3, 4])
    print(v1)

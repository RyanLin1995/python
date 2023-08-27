from array import array
import reprlib
import math
import functools
import operator


class Vector:
    """
    A multi-dimensional ``Vector`` class, take 4

    A ``Vector`` is built from an iterable of numbers::

        >>> Vector([3.1, 4.2])
        Vector([3.1, 4.2])
        >>> Vector((3, 4, 5))
        Vector([3.0, 4.0, 5.0])
        >>> Vector(range(10))
        Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])

    Tests of hashing::

        >>> v1 = Vector([3, 4])
        >>> v2 = Vector([3.1, 4.2])
        >>> v3 = Vector([3, 4, 5])
        >>> v6 = Vector(range(6))
        >>> hash(v1), hash(v3), hash(v6)
        (7, 2, 1)


    Most hash codes of non-integers vary from a 32-bit to 64-bit CPython build::

        >>> import sys
        >>> hash(v2) == (384307168202284039 if sys.maxsize > 2**32 else 357915986)
        True

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

    # tag::VECTOR_V4_HASH[]
    def __eq__(self, other):
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))  # zip 函数的判断需要先判断长度。使用 all 判断所有值结果效率更高

    def __hash__(self):
        hashes = (hash(x) for x in self)  # hashes = map(hash, self)  这个 map 函数更加直观
        return functools.reduce(operator.xor, hashes, 0)  # 使用 operator.xor 函数（异域）计算聚合的哈希值。
        # reduce 的第三个函数是初始值。因为异域的初始值为 0
        # 对于 +、| 和 ^ （异域）initializer 为 0
        # 对于 * 和 & initializer 为 1

    # end::VECTOR_V4_HASH[]

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

    __match_args__ = ('x', 'y', 'z', 't')

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

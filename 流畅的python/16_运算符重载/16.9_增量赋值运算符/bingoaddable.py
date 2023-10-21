"""
======================
AddableBingoCage tests
======================


Tests for __add__:

# tag::ADDABLE_BINGO_ADD_DEMO[]

    >>> vowels = 'AEIOU'
    >>> globe = AddableBingoCage(vowels)  # 创建一个实例
    >>> globe.inspect()
    ('A', 'E', 'I', 'O', 'U')
    >>> globe.pick() in vowels  # 从中取出一项，确保在 vowels 中
    True
    >>> len(globe.inspect())  # 检测长度是否为 4
    4
    >>> globe2 = AddableBingoCage('XYZ')  # 创建第二个实例
    >>> globe3 = globe + globe2
    >>> len(globe3.inspect())  # 将两个实例加在一起，长度为 7
    7
    >>> void = globe + [10, 20]  # 相加只支持同一类型的操作数。错误信息是 __add__ 方法返回 NotImplemented 时 Python 解释器输出的
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for +: 'AddableBingoCage' and 'list'


# end::ADDABLE_BINGO_ADD_DEMO[]

Tests for __iadd__:

# tag::ADDABLE_BINGO_IADD_DEMO[]

    >>> globe_orig = globe  # 创建一个别名
    >>> len(globe.inspect())  # 检测长度
    4
    >>> globe += globe2  # 进行增量赋值运算
    >>> len(globe.inspect())
    7
    >>> globe += ['M', 'N']  # += 右边可以是任何可迭代对象
    >>> len(globe.inspect())
    9
    >>> globe is globe_orig  # 在这个示例中，globe 始终代指 globe_orig
    True
    >>> globe += 1  # 不能和不可迭代对象进行增量赋值运算
    Traceback (most recent call last):
      ...
    TypeError: right operand in += must be 'Tombola' or an iterable

# end::ADDABLE_BINGO_IADD_DEMO[]

"""

# tag::ADDABLE_BINGO[]
from tombola import Tombola
from bingo import BingoCage


class AddableBingoCage(BingoCage):  # 继承于 BingoCage

    def __add__(self, other):
        if isinstance(other, Tombola):  # __add__ 方法的第二个参数只能是 Tombola 实例
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()  # __iadd__ 中，如果是 Tombola 实例则从中获取项
        else:
            try:
                other_iterable = iter(other)  # 否则就创建迭代器
            except TypeError:  # 错误则提示用户处理
                msg = ('right operand in += must be '
                       "'Tombola' or an iterable")
                raise TypeError(msg)
        self.load(other_iterable)
        return self  # 可变对象的增量赋值特殊方法必须返回 self

# end::ADDABLE_BINGO[]

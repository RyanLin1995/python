"""
unrelated.py: examples with ``super()`` in a sibling class.

``U`` is unrelated (does not subclass ``Root``)

Calling ``ping`` on an instance of ``U`` fails::

# tag::UNRELATED_DEMO_1[]
    >>> u = U()
    >>> u.ping()
    Traceback (most recent call last):
      ...
    AttributeError: 'super' object has no attribute 'ping'

# end::UNRELATED_DEMO_1[]


But if ``U`` is part of a cooperative arrangement of base classes,
its ``ping`` method works::

# tag::UNRELATED_DEMO_2[]

    >>> leaf2 = LeafUA()
    >>> leaf2.ping()
    <instance of LeafUA>.ping() in LeafUA
    <instance of LeafUA>.ping() in U
    <instance of LeafUA>.ping() in A
    <instance of LeafUA>.ping() in Root
    >>> LeafUA.__mro__  # doctest:+NORMALIZE_WHITESPACE
    (<class 'diamond2.LeafUA'>, <class 'diamond2.U'>,
     <class 'diamond1.A'>, <class 'diamond1.Root'>, <class 'object'>)

# end::UNRELATED_DEMO_2[]


Here ``U.ping`` is never called because ``Root.ping`` does not call ``super``.

    >>> o6 = LeafAU()
    >>> o6.ping()
    <instance of LeafAU>.ping() in LeafAU
    <instance of LeafAU>.ping() in A
    <instance of LeafAU>.ping() in Root
    >>> LeafAU.__mro__  # doctest:+NORMALIZE_WHITESPACE
    (<class 'diamond2.LeafAU'>, <class 'diamond1.A'>, <class 'diamond1.Root'>,
     <class 'diamond2.U'>, <class 'object'>)

     # 为什么这里 A 之后跟的是 Root 而不是 1 中的 B，是因为 A 跟 U 的父类不一样

"""

# tag::DIAMOND_CLASSES[]
from diamond1 import A


class U():
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()


class LeafUA(U, A):
    def ping(self):
        print(f'{self}.ping() in LeafUA')
        super().ping()


# end::DIAMOND_CLASSES[]

class LeafAU(A, U):
    def ping(self):
        print(f'{self}.ping() in LeafAU')
        super().ping()

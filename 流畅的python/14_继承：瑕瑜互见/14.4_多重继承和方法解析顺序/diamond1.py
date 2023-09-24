"""
diamond1.py: Demo of diamond-shaped class graph.

# tag::LEAF_MRO[]
>>> Leaf.__mro__  # doctest:+NORMALIZE_WHITESPACE
    (<class 'diamond1.Leaf'>, <class 'diamond1.A'>, <class 'diamond1.B'>,
     <class 'diamond1.Root'>, <class 'object'>)

# end::LEAF_MRO[]

# tag::DIAMOND_CALLS[]
    >>> leaf1 = Leaf()
    >>> leaf1.ping()
    <instance of Leaf>.ping() in Leaf
    <instance of Leaf>.ping() in A
    <instance of Leaf>.ping() in B
    <instance of Leaf>.ping() in Root

    >>> leaf1.pong()   # 调用 pong ，唤醒继承树上的 A 中的 pong ，而 A 又调用了 super.pong() 所以会调用 B.pong
    <instance of Leaf>.pong() in A
    <instance of Leaf>.pong() in B

# end::DIAMOND_CALLS[]
"""


# tag::DIAMOND_CLASSES[]
class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'


class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()


class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')


class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()
# end::DIAMOND_CLASSES[]

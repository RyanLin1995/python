# tag::TOMBOLA_BINGO[]

import random

from tombola import Tombola


class BingoCage(Tombola):  # Tombola 子类

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)  # 使用 load 方法实现初始加载

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


# end::TOMBOLA_BINGO[]

b = BingoCage([1, 2, 3, 4, 5])
print(b())

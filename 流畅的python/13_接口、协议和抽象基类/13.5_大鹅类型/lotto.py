# tag::LOTTERY_BLOWER[]

import random

from tombola import Tombola


class LottoBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)  # 初始化方法接收任何可迭代对象，使用传入的参数构建一个列表

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(self._balls)


# end::LOTTERY_BLOWER[]
l = LottoBlower([1, 2, 3, 4, 5])
print(l.pick())

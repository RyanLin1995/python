import random

from collections.abc import Iterable
from typing import TypeVar, Generic

from tombola import Tombola

T = TypeVar('T')


class LottoBlower(Tombola, Generic[T]):  # 泛化类声明通常使用多重继承，因为需要子类化 Generic，以声明形式类型参数

    def __init__(self, items: Iterable[
        T]) -> None:  # __init__ 方法的 items 参数类型是 Iterable[T] 类型。如果使用 LottoBlower[int] 实例化，则类型是 Iterable[int]
        self._balls = list[T](items)

    def load(self, items: Iterable[T]) -> None:  # load 方法有同样的约束
        self._balls.extend(items)

    def pick(self) -> T:  # 如果 LottoBlower[int]，则返回类型 T 会变成 int
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(position)

    def loaded(self) -> bool:
        return bool(self._balls)

    def inspect(self) -> tuple[T, ...]:  # 使用 T 设置返回元组的类型变量
        return tuple(self._balls)

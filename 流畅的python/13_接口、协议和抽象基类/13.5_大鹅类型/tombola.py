# tag::TOMBOLA_ABC[]

import abc


class Tombola(abc.ABC):  # 继承 abc.ABC，定义一个抽象基类

    @abc.abstractmethod
    def load(self, iterable):  # 抽象方法使用 @abc.abstractmethod 标记
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):  # 根据文档说明，如果没有元素可选，抛出 LookupError
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):  # 抽象基类可以包含具体方法
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())  # 抽象基类具体方法只能依赖抽象基类定义的接口

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:  # 因为不知道如何存储元素，因此可以不断调用 pick() 方法清空 self
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)  # 再调用 load 将元素放回去
        return tuple(items)

# end::TOMBOLA_ABC[]

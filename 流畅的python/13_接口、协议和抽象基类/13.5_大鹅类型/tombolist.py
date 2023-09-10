from random import randrange

from tombola import Tombola


@Tombola.register  # 将 Tombolist 注册为 Tombola 的虚拟子类
class TomboList(list):  # TomboList 继承自列表

    def pick(self):
        if self:  # TomboList 从列表继承布尔值行为，可以判断列表是否为空
            position = randrange(len(self))
            return self.pop(position)  # 继承列表后调用 self.pop 方法传入一个随机元素的索引
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # load 使用 list 的 extend 方法

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(self)


# Tombola.register(TomboList)  # 也可以使用这种方法调用 register 进行注册

print(issubclass(TomboList, Tombola))

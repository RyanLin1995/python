import abc


class Validated(abc.ABC):
    def __set_name__(self, owner, name):
        self.storage_name = name

    def __set__(self, instance, value):
        value = self.validate(self.storage_name, value)  # 添加一个新的方法，用于验证。这种设计模式叫自委托（Self-Delegation）
        instance.__dict__[self.storage_name] = value

    @abc.abstractmethod
    def validate(self, name, value):  # 一个抽象方法
        """返回通过验证的值，或抛出ValueError"""


class Quantity(Validated):

    def validate(self, name, value):
        if value <= 0:
            raise ValueError(f'{name} must be > 0')
        return value


class NonBlank(Validated):
    def validate(self, name, value):
        value = value.strip()  # 必须返回的是验证后的数据，防止后续需要清洗这个数据
        if not value:
            raise ValueError(f'{name} cannot be blank')
        return value


class LineItem:
    description = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    raisins = LineItem('1', 10, 6.95)
    print(raisins.__dict__)
    print(raisins.price)

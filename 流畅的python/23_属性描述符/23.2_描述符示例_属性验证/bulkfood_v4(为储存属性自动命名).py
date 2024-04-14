class Quantity:
    def __set_name__(self, owner, name):  # self 是指描述符实例（Quantity），owner 指托管类，name 是在 owner 的类主体中把描述符实例赋给的那个属性的名称
        self.storage_name = name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            msg = f'{self.storage_name} must be > 0'
            raise ValueError(msg)

    # 不需要设置 __get__，因为名称永远一样


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    raisins = LineItem('Golden raisins', 10, 6.95)
    print(raisins.__dict__)
    print(raisins.price)

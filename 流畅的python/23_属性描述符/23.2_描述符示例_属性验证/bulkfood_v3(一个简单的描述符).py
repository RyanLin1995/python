"""

A line item for a bulk food order has description, weight and price fields::

    >>> raisins = LineItem('Golden raisins', 10, 6.95)
    >>> raisins.weight, raisins.description, raisins.price
    (10, 'Golden raisins', 6.95)

A ``subtotal`` method gives the total price for that line item::

    >>> raisins.subtotal()
    69.5

The weight of a ``LineItem`` must be greater than 0::

    >>> raisins.weight = -20
    Traceback (most recent call last):
        ...
    ValueError: weight must be > 0

Negative or 0 price is not acceptable either::

    >>> truffle = LineItem('White truffle', 100, 0)
    Traceback (most recent call last):
        ...
    ValueError: price must be > 0

No change was made::

    >>> raisins.weight
    10

"""


# tag::LINEITEM_QUANTITY_V3[]
class Quantity:  # 描述符基于协议实现，无需子类化

    def __init__(self, storage_name):
        self.storage_name = storage_name  # Quantity 实例有一个 storage_name 属性，这是托管实例中用于存储值的属性的名称

    def __set__(self, instance,
                value):  # 尝试为托管属性赋值时，调用 __set__ 方法。这里，self 是描述符实例（LineItem.weight 或 LineItem.price），instance 是托管实例（LineItem 实例），value 是要设定的值
        if value > 0:
            instance.__dict__[
                self.storage_name] = value  # 必须把属性的值直接存入 __dict__。如果是调用 setattr(instance, self.storage_name)将再次触发 __set__ 方法，导致无限递归
        else:
            msg = f'{self.storage_name} must be > 0'
            raise ValueError(msg)

    def __get__(self, instance, owner):  # 需要实现 __get__ 方法，因为托管属性的名称可能与 storage_name 不同。
        return instance.__dict__[self.storage_name]

    # __get__ 方法有必要实现，因为用户可能编写如下代码。
    # class House:
    #     rooms = Quantity('number of rooms')
    # 在这个 House 类中，托管属性是 rooms，而储存属性是 number_of_rooms。
    # 对于一个名为 chaos_manor 的 House 实例，读写 chaos_manor.rooms 都经过依附在 rooms 上的 Quantity 描述符，
    # 但是读写 chaos_manor.number_of_rooms 会绕过该描述符。

    # 注意，__get__ 方法接受 3 个参数：self、instance 和 owner。
    # owner 参数是对托管类（例如 LineItem）的引用，在希望描述符支持获取类属性时会用到--比如说模拟 Python 获取类属性，但是在实例中未找到指定名称的属性时的默认行为。

    # 如果通过类获取托管属性（例如 LineItem.weight），那么描述符的 get 方法收到的 instance 参数值为 None。
    # 为了支持内省和其他元编程技巧，当通过类存取托管属性时，__get__ 方法最好返回描述符实例。为此，应像下面这样编写 __get__ 方法。
    # def get(self, instance, owner):
    #     if instance is None:
    #         return self
    #     else:
    #         return instance.dict[self.storage_name]


# end::LINEITEM_QUANTITY_V3[]

# tag::LINEITEM_V3[]
class LineItem:
    weight = Quantity('weight')  # 第一个描述符实例管理 weight 属性
    price = Quantity('price')  # 第二个描述符实例管理 price 属性

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
# end::LINEITEM_V3[]

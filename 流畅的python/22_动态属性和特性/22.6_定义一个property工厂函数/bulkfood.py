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
    ValueError: value must be > 0

No change was made::

    >>> raisins.weight
    10

The value of the attributes managed by the properties are stored in
instance attributes, created in each ``LineItem`` instance::

# tag::LINEITEM_V2_PROP_DEMO[]
    >>> nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    >>> nutmeg.weight, nutmeg.price  # 通过 property 读取 weight 和 price，这会遮盖同名实例属性
    (8, 13.95)
    >>> nutmeg.__dict__  # 使用 vars 函数审査 nutmeg 实例，查看真正用于存储值的实例属性。
    {'description': 'Moluccan nutmeg', 'weight': 8, 'price': 13.95}

# end::LINEITEM_V2_PROP_DEMO[]

"""


# tag::LINEITEM_V2_PROP_FACTORY_FUNCTION[]
def quantity(storage_name):  # storage_name 参数确定各个 property 的数据存储在哪里。对 weight property 来说，存储的名称是 weight

    def qty_getter(
            instance):  # qty_getter 函数的第一个参数可以命名为 self，但是这么做很奇怪，因为 qty_getter 函数不在类主体中。instance 指代要把属性存储其中的 LineItem 实例。
        return instance.__dict__[
            storage_name]  # qty_getter 引用了 storage_name，把它保存在这个函数的闭包里。值直接从 instance.__dict__ 中获取，以绕过方法，防止无限递归

    def qty_setter(instance, value):  # 定义 qty_setter 函数，第一个参数也是 instance
        if value > 0:
            instance.__dict__[storage_name] = value  # 将value 直接存入 instance.__dict__，这也是为了绕过方法。
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)  # 构建一个自定义的 property 对象，然后将其返回


# end::LINEITEM_V2_PROP_FACTORY_FUNCTION[]


# tag::LINEITEM_V2_PROP_CLASS[]
class LineItem:
    weight = quantity('weight')  # 使用工厂函数把第一个自定义的 property： weight 定义为类属性
    price = quantity('price')  # 第二次调用，构建另一个自定义的 property，即 price

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # 方法已经激活，确保不能把 weight 设为负数或零
        self.price = price

    def subtotal(self):
        return self.weight * self.price  # 也用到了方法，使用property获取实例中存储的值
# end::LINEITEM_V2_PROP_CLASS[]

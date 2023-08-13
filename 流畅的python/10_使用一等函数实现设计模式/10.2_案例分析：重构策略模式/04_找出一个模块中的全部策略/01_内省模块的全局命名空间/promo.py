from decimal import Decimal
from strategy import Order, Customer, LineItem
from strategy import (
    fidelity_promo, bulk_item_promo, large_order_promo
)

# globals 返回实现当前模块命名空间的字典。通过 globals 模块内省自动找到其他可用的*_promo模块
# 内省：查看对象的类型和属性，查看一个对象是否有某个属性或方法，以及查看对象的文档字符串等
print(globals())
promos = [promo for name, promo in globals().items() if name.endswith('_promo') and name != 'best_promo']


def best_promo(order: Order) -> Decimal:
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)


joe = Customer('John', 0)
ann = Customer('Ann', 1000)
cart = (
    LineItem('banana', 4, Decimal('.5')),
    LineItem('apple', 10, Decimal('1.5')),
    LineItem('watermelon', 5, Decimal('5')),
)
banana_cart = (
    LineItem('banana', 30, Decimal('.5')),
    LineItem('apple', 10, Decimal('1.5')),
)
print(Order(ann, cart, best_promo))

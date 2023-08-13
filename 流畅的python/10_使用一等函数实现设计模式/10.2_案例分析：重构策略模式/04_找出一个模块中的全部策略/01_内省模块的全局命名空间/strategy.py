from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Callable, NamedTuple


class Customer(NamedTuple):  # 带类型的具名元组
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity


@dataclass(frozen=True)  # frozen: 如为真值，则对字段赋值将会产生异常。用于禁止对实例属性重新赋值
class Order:  # 为用户提供服务的上下文
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[
        Callable[['Order'], Decimal]] = None  # 这个类型提示的意思是 promotion 即可以是 None，也可以是接收一个 Order 参数并返回一个 Decimal 值的可调用对象

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))  # 从 start 开始自左向右对 iterable 的项求和并返回总计值

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(
                self)  # 为什么写成 self.promotion(self)? 在 order 类中，promotion 不是方法，而是一个实例属性，只不过它的值是可调用对象。因此，作为表达式的第一部分，self.promotion 的作用是获取可调用对象。为了调用得到的可调用对象，必须提供一个 order 实例，即表达式中的 self。因此，表达式中出现了两个 self。
        return self.total() - discount

    def __repr__(self):
        return f'<order total: {self.total():.2f} due: {self.due():.2f}>'


def fidelity_promo(order: Order):  # 第一个策略
    """为积分为1000或以上的顾客提供5%折扣"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


def bulk_item_promo(order: Order):  # 第二个策略
    """单个商品的数量为20个或以上时提供10%折扣"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


def large_order_promo(order: Order):  # 第三个策略
    """订单中不同商品的数量达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)


def best_promo(order: Order) -> Decimal:
    """选择可用的最佳折扣"""
    promos = [fidelity_promo, bulk_item_promo, large_order_promo]
    return max(promo(order) for promo in promos)

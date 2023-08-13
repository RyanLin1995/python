from decimal import Decimal

from strategy import Order


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

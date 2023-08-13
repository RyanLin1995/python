from decimal import Decimal
import inspect

from strategy import Order
import promotions

# inspect.getmembers 函数用于获取对象的属性，第二个参数是可选的判断条件，返回一个对象上的所有成员，组成以 (名称, 值) 对为元素的列表，按名称排序
promos = [func for _, func in inspect.getmembers(promotions, inspect.isfunction)]


def best_promo(order: Order) -> Decimal:
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)

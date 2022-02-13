# 自定义过滤器
# 过滤器实质上是 Python 的函数
import django.template

# 创建一个 Library 类的对象
register = django.template.Library()


# 自定义过滤器至少有一个参数，最多有两个。
# 一个参数的时候不需要传递，会自动将过滤器前的参数传入，两个参数的时候需要手动传递第二个参数： value|filter: var
@register.filter
def mod(num):
    """判断 num 是否为偶数"""
    return num % 2 == 0


@register.filter
def mod_val(num, val):
    """判断 num 是否能被 val 整除"""
    return num % val == 0
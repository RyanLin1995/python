import time
from functools import wraps


def delayed_start(func=None, *, delay=1):
    """装饰器：在执行被装饰函数前，等待一段时间

    :param delay: 需要等待的秒数
    """

    def decorator(_func):
        @wraps(_func)
        def wrapper(*args, **kwargs):
            print("Waiting {} seconds...".format(delay))
            time.sleep(delay)
            return _func(*args, **kwargs)

        return wrapper

    return decorator(func) if func else decorator


@delayed_start(delay=2)  # 提供 delay=2 参数
def hello1():
    """这是 Hello 1 函数"""
    print("Hello 1")


@delayed_start  # 不提供任何参数，使用默认的 delay=1
def hello2():
    """这是 Hello 2 函数"""
    print("Hello 2")


@delayed_start()  # 不提供任何参数，使用默认的 delay=1，但是是括号调用
def hello3():
    """这是 Hello 3 函数"""
    print("Hello 3")


if __name__ == "__main__":
    print(hello1.__doc__)
    hello1()
    print(hello2.__doc__)
    hello2()
    print(hello3.__doc__)
    hello3()

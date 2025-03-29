import functools
import time
from functools import update_wrapper


class DelayedStart:
    """在执行被装饰函数前，等待一段时间

    :param func: 被装饰的函数
    :param duration: 需要等待的时间
    """

    def __init__(
        self, func, *, duration=1
    ):  # 把 func 以外的参数都定义为 “仅限关键字参数”，从而更好的区分原始函数与装饰器的其它参数
        update_wrapper(self, func)  # 保留被装饰函数的元信息
        self.func = func
        self.duration = duration

    def __call__(
        self, *args, **kwargs
    ):  # 通过实现__call__方法，让实例可以被调用，以此模拟函数调用
        print(f"Wait for 1 second before starting...")
        time.sleep(1)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):  # 为装饰器类定义额外方法，提供更多样化接口
        """跳过等待，立刻执行被装饰器函数"""
        print("Call without delay")
        return self.func(*args, **kwargs)


def delayed_start(**kwargs):
    """装饰器：推迟某个函数的执行"""
    return functools.partial(
        DelayedStart, **kwargs
    )  # 通过 functools.partial 创建一个新的可调用对象，这个对象接受的唯一参数是待装饰函数 func，因此可以用作装饰器


@delayed_start(duration=2)
def hello():
    print("Hello World!")


if __name__ == "__main__":
    print(hello.__name__)
    hello()
    hello.eager_call()

import time
from functools import update_wrapper


class DelayedStart:
    """在执行被装饰函数前，等待1秒"""

    def __init__(self, func):
        update_wrapper(self, func)  # 保留被装饰函数的元信息
        self.func = func

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


@DelayedStart
def hello():
    print("Hello, world!")


if __name__ == "__main__":
    print(hello)  # 函数 hello 已经是 DelayedStart 类型的实例了
    print(
        hello.__name__
    )  # 但是因为 update_wrapper 被调用，hello.__name__ 还是 hello。即还是保存了被装饰函数的元信息
    hello()
    hello.eager_call()

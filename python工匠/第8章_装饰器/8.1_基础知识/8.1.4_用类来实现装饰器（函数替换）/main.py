import time
from functools import wraps


class timer:
    """装饰器：打印函数耗时

    :param print_args: 是否打印方法名和参数，默认为False
    """

    def __init__(self, print_args):
        self.print_args = print_args

    def __call__(self, func, *args, **kwargs):
        @wraps(func)
        def decorated(*args, **kwargs):
            st = time.perf_counter()
            result = func(*args, **kwargs)
            if self.print_args:
                print(f"{func.__name__}, args: {args}, kwargs: {kwargs}")

            print(f"{func.__name__}() 耗时 {time.perf_counter() - st} s")
            return result

        return decorated


@timer(print_args=True)
def hello(name=None):
    time.sleep(1)
    print("hello", name)


if __name__ == "__main__":
    hello("Ryan")

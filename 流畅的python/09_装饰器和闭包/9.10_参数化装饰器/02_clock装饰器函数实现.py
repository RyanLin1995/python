import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):  # 真正的装饰器
        def clocked(*_args):  # 包装被装饰的函数
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(locals())
            print(fmt.format(**locals()))  # **locals() 为了在 fmt 中引用 clocked 的局部变量
            return _result  # clocked 将取代被装饰的函数，因此它应该返回被装饰的函数返回值

        return clocked

    return decorate


if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)

def set_func(func):
    def call_func():
        print("这是一个装饰器")
        func()
    return call_func


@set_func
def test1():
    print("----test1----")


test1()
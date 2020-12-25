def set_func(func):
    print("这是一个装饰器")

    def call_func(*args, **kwargs):
        func(*args, **kwargs)  # 这里传入 *args 跟 **kwargs 是为了拆包，详细可看04_04
        print()
    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("----test1----{}".format(num))
    print("----test1----{}".format(args))
    print("----test1----{}".format(kwargs))


test1(100)
test1(100, 200)
test1(100, 200, 300, mm=100)


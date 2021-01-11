def set_func(func):
    def call_func(*args, **kwargs):
        print("这是一个装饰器")
        return func(*args, **kwargs)  # 这是一个完整的装饰器的写法
    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("----test1----{}".format(num))
    print("----test1----{}".format(args))
    print("----test1----{}".format(kwargs))
    return True, 200, "OK"


@set_func
def test2():
    pass


ret = test1(100)
print(ret)

# 原本 test2() 的返回值就是 None，因此使用装饰器后返回的还是 None
ret = test2()
print(ret)


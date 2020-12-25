def set_func(func):
    print("这是一个装饰器")

    def call_func(a):
        func(a)
        print()
    return call_func


@set_func  # 装饰器在执行到这句话是就开始装饰
def test1(num):
    print("----test1----{}".format(num))


@set_func
def test2(num):
    print("----test2----{}".format(num))

# test1(100)
#
# test1(2013)
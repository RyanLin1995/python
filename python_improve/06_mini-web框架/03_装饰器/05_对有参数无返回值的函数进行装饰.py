def set_func(func):
    def call_func(a):
        print("这是一个装饰器")
        func(a)
        print()
    return call_func


@set_func
def test1(num):
    print("----test1----{}".format(num))


test1(100)

# 100 先作为实参传递到call_func中，即 a = 100。然后把 a 作为实参传递给 func() 函数。此时 func() 指向的是
# test1 的引用。所以 a 等于实参传递到 test1() 中

test1(2013)
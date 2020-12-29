def set_decorator1(func):
    print('这是装饰器1')

    def call_func(*args, **kwargs):
        print("开始装饰1")
        return func(*args, **kwargs)
    return call_func


def set_decorator2(func):
    print('这是装饰器2')

    def call_func(*args, **kwargs):
        print("开始装饰2")
        return func(*args, **kwargs)

    return call_func


# 有结果可知，在装饰时先装饰了 set_decorator2 再 装饰 set_decorator1。是因为装饰器的下一行代码需要是一个函数，那么 set_decorator1 下一行还是装饰器，因此先跳过，先执行 set_decorator2。
# set_decorator2 执行完之后，等价于 test1 = set_decorator2(test1)，那么 set_decorator1 下一行的代码就是一个函数了，就可以开始装饰了。此时的 test1 因为指向了 set_decorator2(test1)，
# 所以最终在执行装饰器代码的过程中，是先执行 set_decorator1 装饰器里面的，再执行 set_decorator2 里面的。
# 即多个装饰器对一个函数进行装饰，装饰的顺序是从下往上，执行的顺序是从上往下
@set_decorator1
@set_decorator2
def test1(*args, **kwargs):
    print("----test1----")


test1()


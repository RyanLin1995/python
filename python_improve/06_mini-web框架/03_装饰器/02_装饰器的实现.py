from functools import warps

def set_func(func):
    @warps(func)  # 装饰器装饰后的函数还拥有原来的属性
    def call_func():
        print("这是一个装饰器")
        func()
    return call_func


# @set_func  # 等价于 test1 = set_func(test1)
def test1():
    print("----test1----")


test1 = set_func(test1)  # Python代码是从右往左执行的，因此左边的 test1 指的是 call_func 这个函数的引用，右边的 test1 指向的是函数
# test1，并作为实参传递到 call_func 中。因此，左边的 test1 的函数内存应该是保存了 func = test1 以及
# call_func() 的代码。test1()看似调用了原本的函数，实际上已经对原本的函数做了修改，但是又不影响原本的函数，

test1()

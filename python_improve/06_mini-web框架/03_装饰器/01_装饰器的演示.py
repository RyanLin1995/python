# 装饰器：可以在保持源代码不变的情况下，在一个已存在函数的代码的前后添加代码

def set_func(func):
    def call_func():
        print("这是一个装饰器")
        func()
    return call_func


@set_func
def test1():
    print("----test1----")


test1()
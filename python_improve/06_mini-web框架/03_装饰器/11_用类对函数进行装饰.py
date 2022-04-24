# 不带参数时的类装饰器
# init ：接收被装饰函数
# call ：实现装饰逻辑

class Test(object):

    def __init__(self, func):  # __init__ 方法接收被装饰的方法

        self.func = func

    def __call__(self, *args, **kwargs):  # __call__ 方法实现方法

        print("这是一个装饰器")
        print("开始装饰")
        return self.func(*args, **kwargs)


@Test
def test():
    print("hahahahah")


test()


# 带参数时的类装饰器
# init ：不再接收被装饰函数，而是接收传入参数
# call ：接收被装饰函数，实现装饰逻辑

class Test(object):

    def __init__(self, loglevel):

        self.loglevel = loglevel

    def __call__(self, func):  # __call__ 方法接收函数
        def wrapper(*args, **kwargs):
            if self.loglevel == 'debug':
                print("这是一个装饰器")
                print("开始装饰")
                print(f'[DEBUG] enter {func.__name__}()')
                func(*args, **kwargs)
                print("装饰结束")
        return wrapper


@Test('debug')
def test():
    print("hahahahah")


test()

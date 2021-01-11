class Test(object):

    def __init__(self, func):

        self.func = func

    def __call__(self, *args, **kwargs):

        print("这是一个装饰器")
        print("开始装饰")
        return self.func(*args, **kwargs)


@Test
def test():
    print("hahahahah")


test()
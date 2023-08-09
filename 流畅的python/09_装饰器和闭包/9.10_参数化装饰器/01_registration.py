registry = set()


def register(active=True):  # 参数化装饰器的工厂函数
    def decorate(func):  # 真正的装饰器
        print(f'running register (active={active})->decorate({func})')

        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func  # 因为 decorate 是装饰器，所以必须返回一个函数

    return decorate  # register 是工厂函数，因此需要返回真正的装饰器函数


@register(active=False)  # register 作为函数调用
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


if __name__ == '__main__':
    print('start')
    print(registry)
    f1()
    print(registry)
    register(active=False)(f2)
    print(registry)

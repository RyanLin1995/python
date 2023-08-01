registry = []


# 装饰器在被装饰函数定义之后立即运行，通常是在导入时
def register(func):  # 定义一个装饰器
    print(f'running register({func})')
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    # register 在模块中会在其他函数之前运行
    main()  # 加载模块后，registry中有两个被装饰函数的引用。这两个函数以及 f3 只在 main 显式调用时才执行

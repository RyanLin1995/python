import sys
import contextlib


@contextlib.contextmanager
def looking_glass():
    """
    使用 @contextmanager 装饰器实现 LookingGlass.而且实现了异常处理
    """
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'RYANLIN'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


@looking_glass()  # 一个小知识，@contextmanager还可以作为装饰器
def verse():
    print('It is a test')


if __name__ == '__main__':
    with looking_glass() as what:
        print(what)
        # print(1 / 0)

    print(what)
    verse()  # looking_glass 在 verse 主体运行前和之后完成了自己的任务
    print('back to normal')

"""
在使用 @contextmanager 装饰的生成器中，yield 把函数的主体分成两部分:
    --> yield 前面的所有代码在with块开始 (解释器调用__enter_方法时)执行
    --> yield 后面的代码在with 块结束时 (调用_exit_方法时)执行
"""
import sys
import contextlib


@contextlib.contextmanager
def looking_glass():
    """
    使用 @contextmanager 装饰器实现 LookingGlass.但是这版本出现错误会在 yield 再次抛出，无法运行 yield 下的语句，导致 sys.stdout.write = original_write 无法执行
    """
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'RYANLIN'  # 如果有错误则在这里抛出异常，没有则将返回值绑定到变量上
    sys.stdout.write = original_write


if __name__ == '__main__':
    with looking_glass() as what:
        print(what)
        print(1 / 0)

    print(what)

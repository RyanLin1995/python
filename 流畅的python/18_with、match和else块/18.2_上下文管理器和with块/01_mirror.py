import sys


class LookingGlass:

    def __enter__(self):  # 上下文管理器接口包含 __enter__ 和 __exit__
        self.original_write = sys.stdout.write  # 把 sys.stdout.write 保存起来供后面使用
        sys.stdout.write = self.reverse_write  # 修改 sys.stdout.write
        return 'RYANLIN'  # 返回数值给传入的目标变量（即 as 后面的变量）

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write  # 还原
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True  # 有异常时返回 True，告诉解释器异常已被处理


if __name__ == '__main__':
    with LookingGlass() as what:
        print('Tea, coffee or me')  # 在上下文管理中，因为 sys.stdout.write 被替换了，所以输出是镜像
        print(what)

    print(what)  # 当退出上下文管理器后，输出变正常，且绑定的目标变量保留了下来

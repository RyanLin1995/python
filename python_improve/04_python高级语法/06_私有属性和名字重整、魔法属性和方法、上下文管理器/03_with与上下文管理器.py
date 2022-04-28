# 对于系统资源如文件,数据库连接,socket等，应用程序打开这些资源并执行完业务逻辑之后，必须做的一件事就是要关闭(断开)该资源。
# 一个程序最多能打开的文件(文件描述符)为1024.如果持续不关闭文件(资源)，会导致资源耗尽
# 而在 Python 程序中，一旦出现错误程序就会奔溃。
# 例如使用 open 打开文件

def m1():
    f = open("output.txt", "w")
    f.write("python之禅")
    f.close()


# 这样写有一个潜在的问题，如果在调用 write 的过程中，出现了异常进而导致后续代码无法继续执行，close
# 方法无法被正常调用，因此资源就会一直被该程序占用。

print("-----------------------")


# 进阶版
def m2():
    f = open("output.txt", "w")
    try:
        f.write("python之禅")
    except IOError:
        print("oops error")
    finally:
        f.close()


# 改良版本的程序是对可能发生异常的代码处进行 try 捕获，使用 try/finally 语句，该语句表示如果在 try
# 代码块中程序出现了异常，后续代码就不再执行，而直接跳转到 except 代码块。而无论如何，finally 块的代码最终都会被执行。因此，只要把
# close 放在 finally 代码中，文件就一定会关闭。 但是如果文件打开环境复杂，存在很多错误情况，那么就要用多个 except 或直接
# except Exception

print("-----------------------")


# 高级版
def m3():
    with open("output.txt", "r") as f:
        f.write("Python之禅")


# 一种更加简洁,优雅的方式就是用 with 关键字。 open 方法的返回值赋值给变量 f，当离开 with 代码块的时候，系统会自动调用
# f.close()方法， with的作用和使用 try/finally 语句是一样的。那么它的实现原理是上下文管理器(Context Manager)。

print("-----------------------")


# 上下文管理器: 实现了__enter__()和__exit__()方法的对象,上下文管理器对象可以使用with关键字
# Demo: 一个实现了上下文管理器的 file 对象

class File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):  # 返回资源对象，这里就是你将要打开的那个文件对象
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):  # 处理一些清除工作。
        print("will exit")
        self.f.close()


# 因为File 类实现了上下文管理器，现在就可以使用with 语句了。
# 上下文管理器执行顺序
# 1. with语句先暂存了File类的__exit__方法
# 2. 然后它调用File类的__enter__方法
# 3. __enter__方法打开文件并返回给with语句
# 4. 打开的文件句柄被传递给opened_file参数
# 5. 使用.write()来写文件
# 6. with语句调用之前暂存的__exit__方法
# 7. __exit__方法关闭了文件

with File('out.txt', 'w') as f:
    print("writing")
    f.write('hello, python')

# 通过 with 调用上下文管理器对象，无需显示地调用close 方法了，由系统自动去调用，哪怕中间遇到异常， close 方法也会被调用。

# 实现上下文管理器的另外方式 Python 还提供了一个contextmanager 的装饰器，更进一步简化了上下文管理器的实现方式。通过yield
# 将函数分割成两部分，yield 之前的语句在__enter__ 方法中执行，yield 之后的语句在__exit__ 方法中执行。紧跟在yield
# 后面的值是函数的返回值。

from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()

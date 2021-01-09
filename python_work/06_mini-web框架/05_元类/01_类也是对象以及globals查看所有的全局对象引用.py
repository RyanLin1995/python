# python 中一切都是对象，类同样也是一种对象
# python 中的print，input等函数为内嵌函数，python 会默认加载
# python 中可以通过 globals 函数查看所有全局对象的引用

a = 100


def test():
    print("I am a test")


print(globals())  # globals 返回的是一个字典，保存的都是全局变量的引用

print(a)  # globals 中存在 a，即globals["a"] = 100，所以能打印a。
print(globals()["a"] == a)

globals()["test"]()

# print(b)  # 因为 globals 中不存在 b，所以打印失败

print(globals()["__builtins__"].__dict__)  # 查看内置函数

# 即当 Python 运行起来的时候，会有一块内存，内存中存储的就是 globals
# 中的数据。如果此时定义了一个函数或类，那么系统就会在分配的内存中创建这个函数或类的空间，
# 然后把名称保存到 globals 中，那么 globals 中保存的变量的名字就指向这个函数或类的空间。
# 也就是说，Python 中所有数据对象都需要空间，那么类也是对象

# 而对于变量，函数或类的寻找顺序：globals --> __builtins__
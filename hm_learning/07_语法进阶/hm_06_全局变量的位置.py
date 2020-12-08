# 注意：在开发时，应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证所有的函数都
# 能够正常的访问到每一个全局变量
num = 10
# 定义一个全局变量
title = "你好吗"
# 在定义一个全局变量
name = "小明"


def demo():
    print("{}".format(num))
    print("{}".format(title))
    print("{}".format(name))


demo()
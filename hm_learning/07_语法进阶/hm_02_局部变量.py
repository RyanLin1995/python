def demo1():
    # 定义一个局部变量
    num = 10

    print("在demo1函数内部的变量是{:g}".format(num))


def demo2():

    num = 99
    print("demo2 ==> {}".format(num))


# 在函数内部定义的变量，不能在其他位置使用
# print("{}".format(num))
demo1()
demo2()

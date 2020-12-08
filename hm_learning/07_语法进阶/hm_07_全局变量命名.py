# 注意：在开发时，应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证所有的函数都
# 能够正常的访问到每一个全局变量
gl_num = 10
# 定义一个全局变量
gl_title = "你好吗"
# 在定义一个全局变量
gl_name = "小明"


def demo():

    # 如果局部变量的名字和全局变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的虚线

    num = 99
    print("{}".format(num))
    print("{}".format(gl_title))
    print("{}".format(gl_name))


demo()
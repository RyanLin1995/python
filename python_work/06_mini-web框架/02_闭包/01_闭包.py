# 问题：以 y = kx + b 为例，计算一条线上的多个点，即给出x求y

# 解决以上问题的方法:
# 第1种：直接写公式
# k = 1
# b = 2
# y = k*x+b
# 缺点：如果需要多次计算，就要写多条公式

print("-"*50)


# 第2种L：函数
def line2(k, b, x):
    print(k*x+b)


line2(1, 2, 0)
line2(1, 2, 1)
line2(1, 2, 2)
# 缺点：如果需要计算多次这条线上的y值，需要多次传递k,b的值

print("-"*50)

# 第3种：全局变量
k = 1
b = 2


def line3(x):
    print(k * x + b)


line3(0)
line3(1)
line3(2)
k = 11
b = 22
line3(0)
line3(1)
line3(2)

# 缺点：如果要计算多条线上的y值，需要每次修改全局变量

print("-"*50)

# 第4种：缺省参数
def line4(x, k=1, b=2):
    print(k * x + b)


line4(0)
line4(1)
line4(2)

line4(0, 11, 22)
line4(1, 11, 22)
line4(2, 11, 22)

# 优点：与全局变量相比，k，b是函数的参数，而不是可以被任意修改的全局变量
# 缺点：如果要计算多条线上的y值，需要每次调用时传递参数

print("-"*50)

# 第5种：实例对象
class Line5(object):

    def __init__(self, k, b):

        self.k = k
        self.b = b

    def __call__(self, x):

        print(self.k * x + self.b)


line5_1 = Line5(1, 2)
line5_1(0)
line5_1(1)
line5_1(2)

line5_2 = Line5(11, 22)
line5_2(0)
line5_2(1)
line5_2(2)

# 优点：基本实现功能
# 缺点：为了计算多条线上的y值，需要创建多个实例对象，浪费资源

print("-"*50)

# 第6种：闭包
# 闭包：嵌套函数。通常情况下外部函数中包含内部函数，且外部函数的值传递到内部函数，并保存在内部函数中。最终由外部函数返回内部函数
def line6(k, b):
    def create_y(x):
        print(k * x + b)
    return create_y


line6_1 = line6(1, 2)  # 该步骤中调用了 line6 函数，并把 k,b 值传入然后 line6 函数的返回值为 create_y 函数，因此 line6_1 中实际上保存了 create_y 函数
line6_1(0)
line6_1(1)
line6_1(2)

line6_2 = line6(11, 22)
line6_2(0)
line6_2(1)
line6_2(2)

# 优点：功能类似于实例对象，但是空间占用很小

print("-"*50)

# 思考：函数、匿名函数、闭包、对象各作为实参时，有什么区别
#1. 匿名函数能完成简单的功能，传递的是这个函数的引用
#2. 普通函数能完成复杂的功能，传递的是这个函数的引用
#3. 闭包能完成较为复杂的功能，传递的事这个闭包中数据及函数，因此传递的是功能+数据
#4. 对象能完成最复杂的功能，传递的是这个对象里面所有的东西，因此传递的是功能+数据

# 修改闭包数据
x = 300


def test1():
    x = 200

    def test2():
        nonlocal x  # 在闭包中使用 nonlocal 修改数据
        print("---1---x={}".format(x))
        x = 100
        print("---2---x={}".format(x))

    return test2


t1 = test1()
t1()
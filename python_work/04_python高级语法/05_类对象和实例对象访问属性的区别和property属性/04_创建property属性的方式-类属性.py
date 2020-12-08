# 使用类属性的方式创建property属性，使用这种方法是，Python2 跟 Python3 区别
################ Demo ################
class Foo(object):

    def get_bar(self):
        return "laowang"

    BAR = property(get_bar)


obj = Foo()
ret = obj.BAR  # 自动调用get_bar方法，并获取方法的返回值
print(ret)

# property方法中有个四个参数:
# 第一个参数是方法名，调用对象.属性时自动触发执行方法
# 第二个参数是方法名，调用对象.属性＝ XXX 时自动触发执行方法
# 第三个参数是方法名，调用del 对象.属性时自动触发执行方法
# 第四个参数是字符串，调用对象.属性.__doc__ ，此参数是该属性的描述信息

# print(help(property))

print("-----------------------------")


############### 案例1 ################
class Foo(object):

    def __init__(self):
        self.value = "laowang"

    def get_bar(self):
        print("getter")
        return self.value

    def set_bar(self, value):
        """必须两个参数"""
        print("setter")
        self.value = value

    def del_bar(self):
        print("deleter")

    BAR = property(get_bar, set_bar, del_bar, "test")


obj = Foo()

# 自动调用第一个参数中定义的获取方法: get_bar
print(obj.BAR)

# 自动调用第二个参数中定义的修改方法: set_bar，并将“xiaowang”当作参数传入
obj.BAR = "xiaowang"
print(obj.BAR)

# 自动调用第三个参数中的定义的删除方法: del_bar (不常用)
del obj.BAR

# 自动调用第四个参数中定义的描述方法: "test" (不常用)
print(Foo.BAR.__doc__)

print("-----------------------------")


############### 案例2 ################
class Goods(object):

    def __init__(self):
        self.original_price = 100
        self.discount = 0.8

    def get_price(self):
        return self.original_price * self.discount

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, "返回商品价格")


obj = Goods()
print(Goods.PRICE.__doc__)  # 查看描述
print(obj.PRICE)  # 获取原本价格
obj.PRICE = 150  # 修改价格
print(obj.PRICE)  # 再次获取价格
del obj.PRICE
print(obj.PRICE)

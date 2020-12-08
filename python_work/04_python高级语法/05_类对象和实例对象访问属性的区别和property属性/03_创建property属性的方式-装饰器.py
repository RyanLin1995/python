# Python2 跟 Python3 中因为使用不同的类，所以调用 property 属性有不同的方法
# 经典类的 property 属性，只有 property 一种装饰器
# ############### 定义 ###############
class Goods:
    @property
    def price(self):
        return "laowang"


# ############### 调用 ###############
obj = Goods()
result = obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
print(result)


# 新式类的 property 属性，具有三种 property 装饰器，分别为 @property(
# 获取属性)，@property方法名.setter(修改属性) 和 @property方法名.deleter(删除属性)
# ############### 定义 ###############
class Goods:
    """python3中默认继承object类
        以python2、3执行此程序的结果不同，因为只有在python3中才有@xxx.setter  @xxx.deleter
    """

    @property
    def price(self):
        print('@property')
        return None

    @price.setter
    def price(self, value):
        print('@price.setter', value)

    @price.deleter
    def price(self):
        print('@price.deleter')


# ############### 调用 ###############
obj = Goods()
print(obj.price)  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
obj.price = 123  # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
del obj.price  # 自动执行 @price.deleter 修饰的 price 方法


# ############### 案例 ################
class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100

        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):

        self.original_price = value

    @price.deleter
    def price(self):

        del self.original_price


obj = Goods()
# 获取商品价格
print(obj.price)

# 设置新的数值后，获取新的价格
obj.price = 200
print(obj.price)

# 删除价格属性
del obj.price
print(obj.price)
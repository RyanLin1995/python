# 使用私有属性定义一个类
class Money(object):

    def __init__(self):

        self.__money = 0

    def get_money(self):

        return self.__money

    def set_money(self, value):

        if isinstance(value, int):
            self.__money = value
        else:
            raise Exception


m = Money()
m.set_money(100)
print(m.get_money())

print("-----------------------------")


# 使用 property 属性升级
class Money(object):

    def __init__(self):

        self.__money = 0

    def get_money(self):

        return self.__money

    def set_money(self, value):

        if isinstance(value, int):
            self.__money = value
        else:
            raise Exception

    Money = property(get_money, set_money)


m = Money()
m.Money = 300
print(m.Money)

print("-----------------------------")


# 使用 property 属性取代
class Money(object):

    def __init__(self):

        self.__money = 0

    @property
    def Money(self):

        return self.__money

    @Money.setter
    def Money(self, value):
        if isinstance(value, int):

            self.__money = value
        else:
            raise Exception


a = Money()
a.Money = 200
print(a.Money)
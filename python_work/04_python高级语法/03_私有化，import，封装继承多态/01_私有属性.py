# xx: 公有属性
# _xx: 私有方法或私有属性，在 from xxx import * 中禁止导入
# __xx: 避免与子类中的属性命名冲突使用的命名，无法被外部直接访问(私有属性或方法)
# __xx__: 魔方属性或对象，如__init__，不要自己发明__这样的命名
# xx_: 避免与Python关键字冲突

class Man(object):

    def __init__(self):
        self.name = "Ray"
        self.__age = 18  # 私有属性

    def manInfo(self):

        print("My name is {} and my age is {}".format(self.name, self.__age))  # 私有属性内部能访问


man = Man()
print(man.name)
print(man.manInfo())
print(man.age)  # 私有属性外界不能访问

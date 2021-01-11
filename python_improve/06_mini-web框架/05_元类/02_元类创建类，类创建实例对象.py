# 元类创建类，类创建实例对象
# 因为类也是对象，你可以在运行时动态的创建它们，就像其他任何对象一样
# Python 中可以使用 type 创建动态的类

class Test1:
    num = 1
    num2 = 200


Test2 = type("Test2", (), {"num": 100, "num2": 200})  # 这里的 type() 就是元类，因为它可以创建类
# type 创建类的格式是 type(类名, 由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

t2 = Test2()
print(t2.num)
print(t2.num2)
help(Test2)  # 用help查看，可以看到 Test2 为类

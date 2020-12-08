# 重写: 在 Python 的类中，如果开发一个类时使用了继承，基类的方法不适合派生类，可以对基类的方法重新写一个同名的方法，这就是重写
# 重载: 定义了两个相同名字的方法，根据方法的类型，参数不一样，将来调用时调用不一样的方法，这就是重载

# 调用被重写的父类方法有三种:
# 1. 父类名.方法名(self, 形参)
# 2. super().方法名(形参)
# 3. super(父类名, self).方法名(形参)
# 但是，如果在多继承中使用了第一种调用父类被重写方法的参数，可能造成父类被多次调用，验证如下:
print("******多继承使用 类名.__init__ 发生的状态******")


class Parent(object):
    def __init__(self, name):
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age):
        print('Son1的init开始被调用')
        self.age = age
        Parent.__init__(self, name)
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, name, gender):
        print('Son2的init开始被调用')
        self.gender = gender
        Parent.__init__(self, name)
        print('Son2的init结束被调用')


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        Son1.__init__(self, name, age)  # 单独调用父类的初始化方法
        Son2.__init__(self, name, gender)
        print('Grandson的init结束被调用')


gs = Grandson('grandson', 12, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)

print("******多继承使用 类名.__init__ 发生的状态******\n\n")

# 因此在多继承推荐使用 super().方法名(形参) 的方式，原因是使用 super() 方法，Python 会利用 C3算法
# 计算出每个类的调用顺序，并确保每个类只被调用一次 最后把结果保存在 __mro__ 方法中，该方法返回的是一个元祖，元祖中的类的顺序为 super(
# ) 的调用顺序验证如下:
print("******多继承使用 super().__init__ 发生的状态******")


class Parent(object):
    def __init__(self, name, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('parent的init开始被调用')
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2的init结束被调用')


class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        # 多继承时，相对于使用 类名.__init__方法，要把每个父类全部写一遍
        # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
        super().__init__(name, age, gender)
        # super(Grandson, self).__init__(name, age, gender)
        # 使用 super(父类名, self).方法名(形参) 这种方法，则指定了父类为哪个类，那么 super() 的调用顺序会以这个父类开始在 mro 中搜寻
        print('Grandson的init结束被调用')


print(Grandson.__mro__)

gs = Grandson('grandson', 12, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)
print("******多继承使用 super().__init__ 发生的状态******\n\n")

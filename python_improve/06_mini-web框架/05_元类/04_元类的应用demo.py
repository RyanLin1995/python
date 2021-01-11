# 究竟为什么要使用元类？
# 究竟是为什么你会去使用这样一种容易出错且晦涩的特性？
# 一般来说，你根本就用不上它：

# “元类就是深度的魔法，99%的用户应该根本不必为此操心。
# 如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。
# 那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。”
# —— Python界的领袖Tim Peters

# 一个例子：把类中的所有类属性从小写改为大写

# 通过属性返回元类
def upper_attr(class_name, class_parents, class_attr):  # 即 type(class_name, class_parents, class_attr) 中的参数传到这个函数中

    # 遍历属性字典，把非__开头的类属性变为大写
    new_attr = {}

    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    # 调用 type 来创建类并返回
    return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):  # 类中的参数 metaclass 指的是用哪个元类创建这个类，如果不添加，默认使用 type 创建。该参数可以传入函数或类

    bar = "bip"


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
f = Foo()
print(f.BAR)


# 通过类返回元类
class UpperAttrMetaClass(type):

    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__

    def __new__(mcs, class_name, class_parents, class_attr):  # 这里因为 UpperAttrMetaClass 作为一个元类，所以 __new__ 不再 cls 方法而是 msc 方法

        # 遍历属性字典，把非__开头的类属性变为大写
        new_attr = {}

        for name, value in class_attr.items():
            if not name.startswith("__"):
                new_attr[name.upper()] = value

        # 调用 type 来创建类并返回
        # 方法1：通过 type 来做类对象的创建
        return type(class_name, class_parents, new_attr)

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程(面向对象编程)，没什么魔法
        # return type.__new__(cls, class_name, class_parents, new_attr)


class Foo(object, metaclass=UpperAttrMetaClass):

    bar = "bip"


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
f = Foo()
print(f.BAR)

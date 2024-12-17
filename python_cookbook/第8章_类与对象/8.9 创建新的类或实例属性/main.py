# 一个描述器就是一个实现了三个核心的属性访问操作(get, set, delete)的类，分别为 __get__() 、__set__() 和 __delete__() 这三个特殊的方法。
# 这些方法接受一个实例作为输入，之后相应的操作实例底层的字典。

# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance,
                cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')  # 使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(2, 3)
    print(p.x)
    p.y = 2.3

    """
    # __get__() 看上去有点复杂的原因归结于实例变量和类变量的不同。如果一个描述器被当做一个类变量来访问，那么 instance 参数被设置成 None 。
    这种情况下，标准做法就是简单的返回这个描述器本身即可 (尽管你还可以添加其他的自定义操作)
    >>> p = Point(2, 3)
    >>> p.x  # Calls Point.x.__get__(p, Point)
    2
    >>> Point.x  # Calls Point.x.__get__(None, Point)
    < __main__.Integer object at 0x100671890 >
    """

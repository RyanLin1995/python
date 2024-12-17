class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    # Getter function
    @property  # property 在新式类中返回属性值，这是装饰器实现方式
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class Person2:
    def __init__(self, first_name):
        self._first_name = first_name

    # Getter function
    def get_name(self):
        return self._first_name

    # Setter function
    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def delete_name(self):
        raise AttributeError("Can't delete attribute")

    first_name = property(get_name, set_name, delete_name)  # 类属性实现方式


# 上述代码中有三个相关联的方法，这三个方法的名字都必须一样。
# 第一个方法是一个 getter 函数，它使得 first_name 成为一个属性。
# 其他两个方法给 first_name 属性添加了 setter 和 deleter 函数。
# 需要强调的是只有在 first_name 属性被创建后，后面的两个装饰器 @first_name.setter 和 @first_name.deleter 才能被定义。

if __name__ == '__main__':
    a = Person('ryan')
    print(a.first_name)
    # a.first_name = 31

    # 一样的效果
    b = Person2('zoe')
    print(b.get_name())
    b.first_name = 27

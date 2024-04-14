from typing import Callable, Any


class Validation:

    def __init__(
            self, validation_function: Callable[[Any], bool], error_msg: str
    ) -> None:
        print("Validation初始化被执行")
        self.validation_function = validation_function  # 传进来的是匿名函数
        self.error_msg = error_msg

    def __call__(self, value):
        print("call被执行")
        if not self.validation_function(value):  # lambda x: isinstance(x, (int, float))
            raise ValueError(f"{value!r} {self.error_msg}")


class Field:  # 描述符类。即实现了描述符协议（即包含 __get__、__set__ 和 __delete__ 方法）的类

    def __init__(self, *validations):  # 用*接收，表示可以传多个，目前代码可以理解为传进来的就是一个个Validation的实例
        print("Field初始化被执行")
        self._name = None
        self.validations = validations  # 接收完后的类型是元组

    def __set_name__(self, owner, name):
        print("set_name被执行")
        self._name = name  # 会自动将托管类ClientClass的类属性descriptor带过来

    def __get__(self, instance, owner):
        print("get被执行")
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def validate(self, value):
        print("验证被执行")
        for validation in self.validations:
            validation(value)  # 这是是将对象当成函数执行时，调用Validation的__call__魔法方法

    def __set__(self, instance, value):
        """
        :param self: 指的是Field对象
        :param instance: ClientClass对象
        :param value: 给属性赋值的值
        :return:
        """
        print("set被执行")
        self.validate(value)
        instance.__dict__[self._name] = value  # 给ClientClass对象赋值  {"descriptor": 42}


class ClientClass:  # 托管类
    descriptor = Field(
        Validation(lambda x: isinstance(x, (int, float)), "is not a number"),
        # Validation(lambda x: x >= 0, "is not >= 0"),
    )


if __name__ == '__main__':
    """
    Validation初始化被执行
    Field初始化被执行
    set_name被执行  # 当Field()赋值给descriptor变量时，执行__set_name__
    ---------------------
    set被执行
    验证被执行
    call被执行
    """
    client = ClientClass()  # 实例化对象
    print("---------------------")
    # 给上面实例化的对象中的属性(Field实例化对象)赋值为42
    client.descriptor = 42

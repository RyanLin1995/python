# tag::RECORD_FACTORY[]
from typing import Union, Any
from collections.abc import Iterable, Iterator

FieldNames = Union[str, Iterable[str]]  # 用户可以使用一整个字符串或产出字符串的可迭代对象提供字符名称


def record_factory(cls_name: str, field_names: FieldNames) -> type[
    tuple]:  # 接收的参数与 collections.namedtuple 的前两个参数类似，返回一个 type，即一个行为类似元组的类

    slots = parse_identifiers(field_names)  # 使用属性名构建一个元组，这将成为新建类的 __slots__ 属性的值

    def __init__(self, *args, **kwargs) -> None:  # 这个函数将成为新建类的 __init__ 方法，接收位置参数和关键字参数
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self) -> Iterator[Any]:  # 按照 __slots__ 设定的顺序产出字段
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):  # 迭代 __slots__ 跟 self,生成友好的字符表示形式
        values = ', '.join(f'{name}={value!r}' for name, value in zip(self.__slots__, self))
        cls_name = self.__class__.__name__
        return f'{cls_name}({values})'

    cls_attrs = dict(  # 组建类属性字典
        __slots__=slots,
        __init__=__init__,
        __iter__=__iter__,
        __repr__=__repr__,
    )

    return type(cls_name, (object,), cls_attrs)  # 调用 type 构造函数，构建新类，然后将其返回


def parse_identifiers(names: FieldNames) -> tuple[str, ...]:
    if isinstance(names, str):
        names = names.replace(',', ' ').split()  # 把以空格或逗号分隔的 names 转换成字符串列表
    if not all(s.isidentifier() for s in names):
        raise ValueError('names must all be valid identifiers')
    return tuple(names)


# end::RECORD_FACTORY[]

if __name__ == '__main__':
    # record_factory: create simple classes just for holding data fields

    # tag::RECORD_FACTORY_DEMO[]
    Dog = record_factory('Dog', 'name weight owner')  # 工厂函数可以想 namedtuple 那样调用：先写类名，后面跟一个字符串，列出属性名称，以空格分开
    rex = Dog('Rex', 30, 'Bob')
    print(rex)  # 友好的字符串表示形式（即调用了 __repr__ ）
    name, weight, _ = rex  # 实例是可迭代对象，因此赋值时可以便利地拆包
    print(name, weight)
    print("{2}'s dog weighs {1}kg".format(*rex))  # 传递给 format 也可以拆包
    rex.weight = 32  # 实例是可变的对象
    print(rex)
    print(Dog.__mro__)  # 新建的类继承自 object，与构建它的工厂函数无关

    # end::RECORD_FACTORY_DEMO[]

    # The factory also accepts a list or tuple of identifiers:
    Dog = record_factory('Dog', ['name', 'weight', 'owner'])
    print(Dog.__slots__)

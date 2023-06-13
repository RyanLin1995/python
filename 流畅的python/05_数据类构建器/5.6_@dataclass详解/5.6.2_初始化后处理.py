from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)  # default_factory 在每次创建数据类实例时调用，构建默认值


@dataclass
class JackerClubMember(ClubMember):
    all_handles = ClassVar[set[str]] = set()  # typing.ClassVar 为伪类型，用于为类变量添加类型提示。
    # all_handles = ClassVar[set[str]] = set() 意思为：all_handles是一个类属性，类型为字符串构成的集合，默认值是一个空集合
    handle: str = ''

    def __post_init__(self):  # __post_init__ 为初始化后处理，用于执行验证以及根据其他字段计算一个字段的值。通常@dataclass在__init__后调用
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)

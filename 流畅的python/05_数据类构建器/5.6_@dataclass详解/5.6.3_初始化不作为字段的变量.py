from dataclasses import dataclass, InitVar


class DatabaseType:
    pass


@dataclass
class C:
    i: int
    j: int = None
    database = InitVar[DatabaseType] = None  # InitVar 为伪类型，可以把不作为实例字段的参数传递给__init__方法。这种参数叫做“仅作初始化的变量”

    # InitVar 阻止 @dataclass 把 database 视为常规字段。database 不会被设为实例属性，亦不出现在dataclass.fields函数返回的列表中。但是生成__init__，database是参数之一

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

from typing import TypeVar, Protocol

T = TypeVar('T')  # 定义一个类型，在 __mul__ 中使用


class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T: ...  # 定义一个 Protocol 类，该协议类有方法 __mul__。该类型接受任何能实现 __mul__ 函数的对象


RT = TypeVar('RT', bound=Repeatable)  # 定义一个名为 RT 的类型，并将该类型绑定（bound）到 Repeatable


def double(x: RT) -> RT:  # 现在类型检查工具可以确认 x 参数是一个可以乘以整数的对象，返回值类型与 x 相同（即传入值是什么，返回值就是什么）
    return x * 2

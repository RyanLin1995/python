# tag::BEVERAGE_TYPES[]
from typing import TypeVar, Generic


class Beverage:
    """任何饮料"""


class Juice(Beverage):
    """任何果汁"""


class OrangeJuice(Juice):
    """橙汁"""


T = TypeVar('T')  # 简单的 TypeVar 声明


class BeverageDispenser(Generic[T]):  # 参数化饮料类型
    """一个参数化饮料类型的自动售货机"""

    def __init__(self, beverage: T) -> None:
        self.beverage = beverage

    def dispense(self) -> T:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:  # <4>
    """安装一个果汁自动售货机"""


# end::BEVERAGE_TYPES[]

################################################ exact type

# tag::INSTALL_JUICE_DISPENSER[]
juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser)
# end::INSTALL_JUICE_DISPENSER[]


################################################ variant dispenser

# tag::INSTALL_BEVERAGE_DISPENSER[]
beverage_dispenser = BeverageDispenser(Beverage())
install(beverage_dispenser)
## mypy: Argument 1 to "install" has
## incompatible type "BeverageDispenser[Beverage]"
##          expected "BeverageDispenser[Juice]"
# end::INSTALL_BEVERAGE_DISPENSER[]


################################################ variant dispenser

# tag::INSTALL_ORANGE_JUICE_DISPENSER[]
orange_juice_dispenser = BeverageDispenser(OrangeJuice())
install(
    orange_juice_dispenser)  # 使用 orangeJuice 特化的自动售货机也不允许安装，只允许安装 BeverageDispenser[Juice].BeverageDispenser[OrangeJuice] 与 BeverageDispenser[Juice]不兼容(尽管 OrangeJuice是Juice 的子类型)，按照类型相关的术语，我们说 BeverageDispenser(Generic[T])是不变的# 诸如 list 和 set 之类 Python 可变的容器类型都是不变的。
## mypy: Argument 1 to "install" has
## incompatible type "BeverageDispenser[OrangeJuice]"
##          expected "BeverageDispenser[Juice]"
# end::INSTALL_ORANGE_JUICE_DISPENSER[]

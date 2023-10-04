from typing import TypeVar, Generic


class Beverage:
    """任何饮料"""


class Juice(Beverage):
    """任何果汁"""


class OrangeJuice(Juice):
    """橙汁"""


# tag::BEVERAGE_TYPES[]
T_co = TypeVar('T_co', covariant=True)  # 声明类型变量时，设置 covariant=True 表明这是协变的类型参数。_co 后缀是 typeshed 项目采用的一种约定


class BeverageDispenser(Generic[T_co]):  # 使用 T_co 参数化特殊的 Generic 类
    def __init__(self, beverage: T_co) -> None:
        self.beverage = beverage

    def dispense(self) -> T_co:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
    """安装一个果汁自动售货机"""


# end::BEVERAGE_TYPES[]

################################################ covariant dispenser

# tag::INSTALL_JUICE_DISPENSERS[]
juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser)

orange_juice_dispenser = BeverageDispenser(OrangeJuice())  # 现在对可协变的 BeverageDispenser 来说，Juice 和 OrangeJuice两者都是有效
install(orange_juice_dispenser)
# end::INSTALL_JUICE_DISPENSERS[]

################################################ more general dispenser

# tag::INSTALL_BEVERAGE_DISPENSER[]
beverage_dispenser = BeverageDispenser(Beverage())
install(beverage_dispenser)
## mypy: Argument 1 to "install" has
## incompatible type "BeverageDispenser[Beverage]"
##          expected "BeverageDispenser[Juice]"
# end::INSTALL_BEVERAGE_DISPENSER[]

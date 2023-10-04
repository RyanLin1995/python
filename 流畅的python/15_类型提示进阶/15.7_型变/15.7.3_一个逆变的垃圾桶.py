# tag::TRASH_TYPES[]
from typing import TypeVar, Generic


class Refuse:
    """任何废弃物"""


class Biodegradable(Refuse):
    """可生物降解的废弃物"""


class Compostable(Biodegradable):
    """可制成肥料的废弃物，但不是所有可降解废弃物都可以制作成肥料"""


T_contra = TypeVar('T_contra', contravariant=True)  # _contra 表示逆变类型变量


class TrashCan(Generic[T_contra]):  # TrashCan 对废弃物的类型实行逆变
    def put(self, refuse: T_contra) -> None:
        """在倾倒之前存放垃圾"""


def deploy(trash_can: TrashCan[Biodegradable]):
    """放置一个垃圾桶，存放可生物降解废弃物"""


# end::TRASH_TYPES[]


################################################ contravariant trash can


# tag::DEPLOY_TRASH_CANS[]
bio_can: TrashCan[Biodegradable] = TrashCan()
deploy(bio_can)

trash_can: TrashCan[Refuse] = TrashCan()
deploy(trash_can)
# end::DEPLOY_TRASH_CANS[]


################################################ more specific trash can

# tag::DEPLOY_NOT_VALID[]
compost_can: TrashCan[Compostable] = TrashCan()
deploy(
    compost_can)  # 更一般的 TrashCan[Refuse] 是可接受的，因为它可以存放任何废弃物，包括可生物降解的废弃物 (Biodegradable)。然而，TrashCan[Compostable] 不可接受，因为它不能存放可生物降解的废弃物 (Biodegradable)。
## mypy: Argument 1 to "deploy" has
## incompatible type "TrashCan[Compostable]"
##          expected "TrashCan[Biodegradable]"
# end::DEPLOY_NOT_VALID[]

from dataclasses import dataclass, field, fields
from datetime import date
from enum import Enum, auto
from typing import Optional, List


class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    """描述媒体资源"""
    identifier: str
    title: str = '<untitled>'
    creators: List[str] = field(default_factory=list)
    date: Optional[date] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subject: List[str] = field(default_factory=list)

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        ident = ' ' * 4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{ident}{f.name} = {value!r}')

        res.append(')')
        return '\n'.join(res)


if __name__ == '__main__':
    print(repr(Resource('123', 'test', ['a', 'b'], date.today(), ResourceType.BOOK, 'test', 'CN', ['c', 'd'])))

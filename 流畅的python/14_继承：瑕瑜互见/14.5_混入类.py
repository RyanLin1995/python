# tag::UPPERCASE_MIXIN[]
import collections


def _upper(key):  # 这个辅助函数的 key 接收任何类型的参数，并尝试返回 key.upper() ，如果失败则返回 key
    try:
        return key.upper()
    except AttributeError:
        return key


class UpperCaseMixin:  # 这个混入类实现四个基本方法
    def __setitem__(self, key, item):
        super().__setitem__(_upper(key), item)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, key):
        return super().__contains__(_upper(key))


# end::UPPERCASE_MIXIN[]

# tag::UPPERDICT[]
class UpperDict(UpperCaseMixin, collections.UserDict):  # 使用混合类时，混合类必须是基类（即第一个）
    pass


class UpperCounter(UpperCaseMixin, collections.Counter):
    """一个特殊的计数器，字符串是大写形式"""


# end::UPPERDICT[]


if __name__ == '__main__':
    # tag::UPPERDICT_DEMO[]
    d = UpperDict([('a', 'letter A'), (2, 'digit two')])
    print(list(d.keys()))
    d['b'] = 'letter B'
    print('b' in d)
    print(d['a'], d.get('B'))
    print(list(d.keys()))
    # end::UPPERDICT_DEMO[]

    # And ``UpperCounter`` is also case - insensitive:

    # tag::UPPERCOUNTER_DEMO[]
    c = UpperCounter('BaNanA')
    print(c.most_common())

    # end::UPPERCOUNTER_DEMO[]

    # Detailed tests
    # == == == == == == ==
    # UpperDict uppercases all string keys.
    d = UpperDict([('a', 'letter A'), ('B', 'letter B'), (2, 'digit two')])
    # Tests for item retrieval using `d[key]` notation:
    print(d['A'], d['b'], d[2])

    # Tests for missing key:
    # print(d['z'])
    # print(d[99])

    # Tests for item retrieval using `d.get(key)` notation:
    print(d.get('a'), d.get('B'), d.get(2), d.get('z', '(not found)'))

    # Tests for the ` in ` operator:
    print(('a' in d, 'B' in d, 'z' in d))

    # Test for item assignment using lowercase key:
    d['c'] = 'letter C'
    print(d['C'])

    # Tests for update using a `dict` or a sequence of pairs:
    d.update({'D': 'letter D', 'e': 'letter E'})
    print(list(d.keys()))
    d.update([('f', 'letter F'), ('G', 'letter G')])
    print(list(d.keys()))
    print(d)

    # UpperCounter uppercases all `str` keys.

    # Test for initializer: keys are uppercased.
    d = UpperCounter('AbracAdaBrA')
    print(sorted(d.keys()))

    # Tests for count retrieval using `d[key]` notation:
    print(d['a'])
    print(d['z'])

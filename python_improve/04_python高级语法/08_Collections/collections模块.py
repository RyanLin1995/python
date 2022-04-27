import enum
from collections import defaultdict, Counter, deque, namedtuple, ChainMap
from enum import Enum, auto

# defaultdict
# defaultdict 返回一个新的类似字典的对象。
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)  # defaultdict 创建一个字典，默认值是空列表
for k, v in s:
    d.setdefault(k, []).append(v)

print(sorted(d.items()))

# defaultdict 面试题
"""
有如下两个列表：
a = ['a,1', 'b,3,22', 'c,3,4', 'f,5', ]
b = ['a,2', 'b,4', 'w,12', 'd,2','c,123']
需要将两个列表中有相同字母的字符串合并，合并后的结果如下：
c = ['a,1,2', 'b,3,22,4', 'c,3,4,123', 'f,5', 'w,12', 'd,2']
"""

a = ['a,1', 'b,3,22', 'c,3,4', 'f,5', ]
b = ['a,2', 'b,4', 'w,12', 'd,2', 'c,123']
dct = defaultdict(str)
for i in a:
    dct[i[0]] = i

for j in b:
    if j[0] in dct:
        dct[j[0]] += j[1:]
    else:
        dct[j[0]] = j[1:]

print(dict(dct))
print(dct.values())

print('-' * 20)
# Counter
# Counter 是一个简单的计数器，可以针对某项数据进行计数。
# 它是一个集合，元素像字典键(key)一样存储，值为计数存储
# Counter 的基本用法
# Counter('gallahad')  # iterable
# Counter({'red': 4, 'blue': 2})  # mapping
# Counter(cats=4, dogs=8)  # keywords arguments
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)
favs = Counter(name for name, colour in colours)
print(favs)
print(favs.most_common(3))  # 返回最常见的3个元素

# subtract()
# subtract() 方法用于减去另一个计数器或者字典的值。
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
print(c - d)

# Counter 面试题
'''
编写Python脚本，分析xx.log文件，按域名统计访问次数

xx.log文件内容如下：
https://www.sogo.com/ale.html
https://www.qq.com/3asd.html
https://www.sogo.com/teoans.html
https://www.bilibili.com/2
https://www.sogo.com/asd_sa.html
https://y.qq.com/
https://www.bilibili.com/1
https://dig.chouti.com/
https://www.bilibili.com/imd.html
https://www.bilibili.com/

输出：
4 www.bilibili.com
3 www.sogo.com
1 www.qq.com
1 y.qq.com
1 dig.chouti.com
'''


def count_domain(file_path):
    with open(file_path, 'r') as f:
        reader = f.read()
        domain_list = []
        for domain in reader.split('\n'):
            domain_list.append(domain.split('/')[2])
        return Counter(domain_list).most_common(5)


for i in count_domain('xx.log'):
    print(i[1], i[0])

print('-' * 20)
# deque
# deque 是一个双端队列，可以从两端添加和删除元素。
d = deque()  # 如果没有指定参数maxlen，默认创建一个空的双端队列，
# 如果指定了参数，则创建一个长度为参数的双端队列。当数据量超过队列长度时，最左端数据会被删除。
d.append(1)
d.append(2)
d.append(3)

print(len(d))
print(d)

d = deque(range(5))
d.popleft()  # 移除并返回 deque 最左边的元素，没有的话引发 IndexError
d.pop()  # 移除并返回 deque 最右边的元素，没有的话引发 IndexError
for i in d:
    print(i)

print('-' * 20)
# namedtuple
# namedtuple 命名元素，使元组可以像字典那样通过字段名来获取属性，同样可以通过索引和迭代获取
Point = namedtuple('Point_test', ['x', 'y'])
p = Point(11, 22)
print(p)
print(p.x)
print(p[0])

# _make() 方法可以将一个存在的序列或迭代实例创建一个新 namedtuple 实例
a = [33, 44]
p = Point._make(a)
print(p)

# _asdict() 方法将 namedtuple 转化为新的 dict
dict_p = p._asdict()
print(dict_p)

print('-' * 20)


# enum.Enum
# enum.Enum  枚举对象，可将过个唯一常量值绑定一组符号名（即成员）
# 枚举表示的是常量，因此，建议枚举成员名称使用大写字母


@enum.unique  # 默认情况下，枚举允许多个名称作为一个值的别名。@enum.unique 禁用此行为
class Color(Enum):  # 类 Color 是枚举的子类
    RED = 1  # 枚举成员，同是也是常量，具有名称和值，名称为 RED，值为 1
    GREEN = 2
    BLUE = 3
    # 两个枚举成员不能有相同的名称，否则会报错，但是可以有相同的值。
    # 假设，成员 A 和 B 的值相同（先定义的是 A），则 B 是 A 的别名。
    # 按值查找 A 和 B 的值返回的是 A。按名称查找 B，返回的也是 A
    # PINK = 3  # 因为存在 @enum.unique，因此这里会报错

    YELLOW = auto()  # auto() 方法可以自动设定常量值


print(list(Color))

# 获取枚举成员
print(Color(1))
print(Color.RED)
print(Color['RED'])

# 获取枚举成员的名称
print(Color(1).name)
print(Color.RED.name)
print(Color['RED'].name)

# 获取枚举成员属性的方法
print(Color.RED.value)
print(Color['RED'].value)
print(Color(1).value)

print(Color.YELLOW)
print(Color.YELLOW.name)
print(Color.YELLOW.value)

print('-' * 20)
# ChainMap
# ChainMap 将多个映射快速的链接到一起，创建一个单独的可更新的试图
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
chain = ChainMap(baseline, adjustments)
print(chain)
print(list(chain))
# 很多 dict 的方法使用于 ChainMap 中
for k, v in chain.items():
    print(k, v)

print(chain['music'])

# ChainMap 的增删改只对第一个映射起作用，同时会修改源字典
chain['art'] = "new string"
print(chain)
print(baseline)
del chain['music']
print(chain)
print(baseline)
# del chain['opera']  # 会报错
# print(adjustments)

# new_child() 方法实质上是在列表的第一个元素前放入一个字典并返回这个类似列表的对象，默认是 {}
child_chain = chain.new_child()
print(child_chain)

# parents() 方法返回一个新的 ChainMap 包含所有的当前实例的映射，除了第一个
parent_chain = chain.parents
print(parent_chain)
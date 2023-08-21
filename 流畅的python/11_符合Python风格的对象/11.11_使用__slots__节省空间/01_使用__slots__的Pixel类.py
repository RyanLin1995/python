# 默认情况下，Python 把各个实例的属性存储在一个名为__dict__的字典中，其消耗的内存很多。
# 但是，如果定义一个名为 __slots__的类属性，以序列的形式存储属性名称，那么 Python 将使用其他模型存储实例属性，消耗的内存比字典少。
class Pixel:
    __slots__ = ('x', 'y')  # slots 需要在定义类时声明，之后添加或修改均无效。属性名称可以存放在一个元组或列表中


p = Pixel()
# print(p.__dict__)  # Pixel 实例没有 __dict__ 属性
p.x = 10  # 存在于 __slots__ 的属性可以正常复制
p.y = 20


# p.color = 'red'  # 不存在于 __slots__ 的属性会抛出 AttributeError


class OpenPixel(Pixel):  # 子类只继承__slots__ 的部分效果。要确保子类的实例也没有 __dict__ 属性，必须在子类中再次声明 __slots__
    pass


op = OpenPixel()
print(op.__dict__)  # 继承于 Pixel 的子类有 __dict__ 属性
op.x = 8
print(op.__dict__)  # 即使设定 x 属性，也不存入 __dict__ 属性
op.color = 'red'
print(op.__dict__)  # 不存在于__slots__的属性，则存入 __dict__ 属性


class ColorPixel(Pixel):
    # __slots__ = ()  # 如果子类中声明 __slots__ = ()(一个空元组)，则子类实例没有 __dict__，且只接受基类 __slots__ 的属性
    __slots__ = ('color',)  # 如果子类需要额外属性，需在子类 __slots__ 中列出来


cp = ColorPixel()
print(cp.__dict__)  # 会报错
cp.x = 2
cp.color = 'red'

from collections import abc


class FrozenJSON:
    """A read-only façade for navigating a JSON-like object
       using attribute notation
    """

    def __init__(self, mapping):
        self.data = dict(mapping)  # 使用 mapping 参数构建一个字典。这么做是为了确保传入的映射或其他对象可以转换成字典。-data 前面有两条下划线，是私有属性。

    def __getattr__(self, name):  # 仅当未指定名称(name)的属性时才调用__getattr__方法
        try:
            return getattr(self.data,
                           name)  # 如果 name 匹配 __data 字典的某个属性，就返回对应的属性。feed.keys() 调用就是这样处理的: keys方法是 __data 字典的一个属性。
        except AttributeError:
            return FrozenJSON.build(
                self.data[name])  # 否则，从 self.__data 中获取 name 键对应的项，返回调用 FrozenJsoN.build() 方法得到的结果。

    def __dir__(
            self):  # 实现为内置函数 dir()提供支持的 __dir__ 方法，进而支持在 Python 标准控制台，以及 IPython、Jupyter Notebook 等中自动补全。这个方法的代码很简单，将基于 self.__data 中的键实现递归自动补全，因为 __getattr__ 方法能即时构建 FrozenJSON 实例--方便采用交互方式探索数据。
        return self.data.keys()

    @classmethod
    def build(cls, obj):  # 这是一个备选构造方法，是 @classmethod 装饰器的常见用途
        if isinstance(obj, abc.Mapping):  # 如果 obj 是一个映射，那么就构建一个 FrozenJSON 对象。这里利用了大鹅类型
            return cls(obj)
        elif isinstance(obj,
                        abc.MutableSequence):  # 如果是一个 MutableSequence 对象，则必然是列表，因此，把 obj 中的每一项递归都传给 .build() 方法，构建一个列表。
            return [cls.build(item) for item in obj]
        else:  # 如果既不是字典也不是列表，那么原封不动返回项
            return obj


if __name__ == '__main__':
    import json

    raw_feed = json.load(open('data/osconfeed.json'))
    feed = FrozenJSON(raw_feed)
    print(feed)
    print(len(feed.Schedule.speakers))
    print(feed.keys())
    print(sorted(feed.Schedule.keys()))
    for key, value in sorted(feed.Schedule.items()):
        print(f'{len(value):3} {key}')
    print(feed.Schedule.speakers[-1].name)
    talk = feed.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk.flavor)

    # FrozenJSON 实例的私有实例属性 __data 存储在 FrozenJSON data名下。尝试通过其他名称获取属性将触发 __getattr__ 方法。
    # 这个方法会先查看 self.__data 字典有没有指定名称的属性(不是键)，这样 FrozenJS0N 实例便可以处理 dict 的方法，例如把 items 方法委托给 self.__data.items()。
    # 如果 self.__data 没有指定名称的属性，那么 __getattr__ 方法就会以那个名称为键，从 self.__data 中获取一项，传给 FrozenJSON.build() 方法。
    # 这样便能深入 JSON 数据的嵌套结构，使用类方法 build 把每一层嵌套都转换成一个 FrozenJSON 实例。

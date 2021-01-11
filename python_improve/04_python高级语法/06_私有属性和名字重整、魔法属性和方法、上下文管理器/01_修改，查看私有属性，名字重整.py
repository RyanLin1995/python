# 当一个类定义了一个私有属性时，是不能被调用的
class Test(object):

    def __init__(self, name):

        self.__name = name


t = Test("laowang")
# print(t.__name)  # 出现错误，因为不能直接调用私有属性

print(t.__dict__)  # 通过 __dict__ 魔法属性发现，私有属性被改名了，因此不能被直接调用
print(t._Test__name)  # 通过新的属性名调用私有属性成功

t.__name = "xiaowang"  # 通过 __name 对私有属性改名，发现没改成功。意味着 t.__name
# 只是对实例对象添加了一个名为 __name 的属性(不是公有也不是私有属性)
print(t.__dict__)
print(t.__name)
print(t._Test__name)
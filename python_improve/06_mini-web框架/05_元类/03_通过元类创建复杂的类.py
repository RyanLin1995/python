# 首先创建一个基本的类
Test1 = type("Test1", (), {"num": 100, "num2": 200})  # 这个代码一共有两个 Test，第一个 Test 指的是变量名，指 Test 这个变量指向了 type() 函数的指向。
#第二个 Test 指的是 type 类型的第一个参数，即元类的名称。一般建议将变量名设置为元类的名称

print(help(Test1))

print("*" * 50)


# 元类添加实例方法
def test2(self):
    print("这是一个实例方法")
    print("*" * 50)


Test2 = type("Test2", (Test1,), {"test2":test2})

print(Test2().test2())
print(help(Test2))

print("*" * 50)

# 元类添加类方法
@classmethod
def test3(cls):
    print("一个类方法")
    print("*" * 50)


Test3 = type("Test3", (Test2,), {"test3": test3})

print(Test3().test3())
print(help(Test3))

print("*" * 50)


# 元类添加静态方法
@staticmethod
def test4():
    print("静态方法")
    print("*" * 50)


Test4 = type("Test4", (Test3,), {"test4": test4})

print(Test4().test4())
print(help(Test4))

print("*" * 50)


# 类中通过 __class__ 可以知道实例属性由谁创建，由此可以所有类的创建者为type
class Test5(object):
    pass


t5 = Test5()
print(t5.__class__)
print(t5.__class__.__class__)
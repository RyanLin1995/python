class Class:  # 定义Class 类，这个类有两个类属性: data 属性和 prop 特性。
    data = 'the class data attr'

    @property
    def prop(self):
        return 'the prop value'


if __name__ == '__main__':
    obj = Class()

    # 实例属性遮盖类属性
    print(vars(obj))  # vars 函数返回 obj 的 dict 属性，可以看到，没有实例属性。
    print(obj.data)  # 读取 obj.data，获取的是 class.data 的值。
    obj.data = 'bar'  # 为 obj.data 赋值，创建一个实例属性。
    print(vars(obj))  # 审查实例，查看实例属性。
    print(obj.data)  # 现在读取 obj.data，获取的是实例属性的值。从obj实例中读取属性时，实例属性 data 遮盖类属性 data。
    print(Class.data)  # Class.data 属性的值完好无损

    print('-' * 52)

    # 实例属性不遮盖类方法
    print(Class.prop)  # 直接从 Class 中读取 prop 方法，获取的是 property 对象本身，不运行 property 的读值方法
    print(obj.prop)  # 读取 obj.prop 执行 property 的读值方法
    # obj.prop = 'foo'  # 尝试设置 prop 实例属性，结果失败了
    obj.__dict__['prop'] = 'foo'  # 但是可以直接把 'prop' 存入 obj.__dict__
    print(vars(obj))  # 可以看到，obj 现在有两个实例属性: data 和 prop
    print(obj.prop)  # 然而，读取 obj.prop 时仍会运行 property 的读值方法。property 未被实例属性遮盖
    Class.prop = 'baz'  # 覆盖 Class.prop 方法，销毁方法对象
    print(obj.prop)  # 现在，obj.prop 获取的是实例属性。Class.prop 不是方法了，因此不再覆盖 obj.prop。

    print('-' * 52)

    # 新添加的类方法遮盖现有的实例属性
    print(obj.data)  # obj.data 获取的是实例属性 data
    print(Class.data)  # Class.data 获取的是类属性 data
    Class.data = property(lambda self: 'the "data" prop value')  # 使用新方法覆盖 Class.data
    print(obj.data)  # 现在 obj.data 被 Class.data 方法遮盖了
    del Class.data  # 删除方法
    print(obj.data)  # 现在恢复原样，obj.data 获取的是实例属性 data。

    # 总结：像 obj.data 这样的表达式不会从 obj 而是从 obj.__data__ 开始寻找 data，而且仅当类中没有名为 data 的 property 时，Python 才会在 obj 实例中寻找。

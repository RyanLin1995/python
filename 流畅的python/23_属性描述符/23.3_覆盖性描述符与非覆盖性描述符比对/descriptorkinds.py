# tag::DESCR_KINDS[]

### 仅用于显示的辅助功能 ###

def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return f'<class {obj.__name__}>'
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return f'<{cls_name(obj)} object>'


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print(f'-> {cls_name(args[0])}.__{name}__({pseudo_args})')


### 本例中的必备类 ###

class Overriding:  # 具有 __get__ 方法和 __set__ 方法的覆盖型描述符
    """又称数据描述符或覆盖描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)  # 这个实例中，所有的描述符都调用了 print_args 函数

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:  # 没有 __get__ 方法的覆盖型描述符
    """一个没有 ``__get__`` 的覆盖描述符"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:  # 没有 __set__ 方法的非覆盖型描述符
    """又称非数据或非覆盖型描述符"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:  # 托管类
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):  # 作对比，因为方法也是描述符
        print(f'-> Managed.spam({display(self)})')


# end::DESCR_KINDS[]

if __name__ == '__main__':
    obj = Managed()
    # 覆盖性描述符行为
    obj.over
    Managed.over
    obj.over = 7
    obj.over
    print(vars(obj))
    obj.__dict__['over'] = 8
    print(vars(obj))
    obj.over

    print('-' * 50)

    # 没有 __get__ 方法的覆盖型描述符
    print(obj.over_no_get)  # 这个描述符没有 __get__ 方法，因此从类中获取描述符实例
    print(Managed.over_no_get)
    obj.over_no_get = 7  # 为 obj.over_no_get 赋值，调用的是描述符 __set__ 方法
    print(obj.over_no_get)  # 因为 __set__ 没有修改属性，所以再次读取 obj.over_no_get 获取的还是托管类中描述符的实例
    obj.__dict__['over_no_get'] = 9  # 通过实例 __dict__ 设置同名值
    print(obj.over_no_get)  # 现在，obj.over_no_get 实例属性遮盖描述符，但是只有读操作
    obj.over_no_get = 7  # 为 obj.over_no_get 赋值，仍然通过描述符 __set__ 方法处理
    print(obj.over_no_get)  # 但是读取时，只要有同名的实例属性，描述符就会被遮盖

    print('-' * 50)

    # 一个非覆盖型描述符的行为
    obj.non_over  # 触发描述符 __get__ 方法，传入的第二个参数是 obj
    obj.non_over = 7  # Managed.non_over 是非覆盖类型描述符，没有干涉赋值操作的 __set__ 方法
    print(obj.non_over)  # 现在，obj 有个名为 non_over 的实例属性，会遮盖 Managed 类的同名描述符属性
    Managed.non_over  # Managed.non_over 描述符依旧存在，但是会通过类截取这次访问
    del obj.non_over  # 如果删掉 non_over 实例属性，那么读取 obj.non_over 时会触发类中描述符的 __get__ 方法。但是第二个参数依旧是托管类的实例
    obj.non_over

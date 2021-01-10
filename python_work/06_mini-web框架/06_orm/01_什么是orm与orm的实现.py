# ORM(Object Relational Mapping) 是 python编程语言后端web框架 Django 的核心思想，即对象-关系映射
# 一般应用于创建一个实例对象，用创建它的类名当做数据表名，用创建它的类属性对应数据表的字段，当对这个实例对象操作时，能够进行对应 MySQL 语句的操作
# 实际上所谓的ORM就是让开发者在操作数据库的时候，能够像操作对象时通过 xxxx.属性=yyyy 一样简单，这是开发ORM的初衷

# orm 的实现
class ModelMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        mappings = dict()

        # 将 attrs 字典中，值为元祖的加到字典中
        for k, v in attrs.items():

            if isinstance(v, tuple):  # 判断值是否为元祖
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 删除 attrs 中与 mappings 冲突的键
        for k in mappings.keys():
            attrs.pop(k)

        # 将之前的uid/name/email/password以及对应的对象引用、类名字添加到 attrs 中
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(mcs, name, bases, attrs)


class User(metaclass=ModelMetaclass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")
    # 当指定元类之后，以上的类属性将不在类中，而是在__mappings__属性指定的字典中存储
    # 以上User类中有
    # __mappings__ = {
    #     "uid": ('uid', "int unsigned")
    #     "name": ('username', "varchar(30)")
    #     "email": ('email', "varchar(30)")
    #     "password": ('password', "varchar(30)")
    # }
    # __table__ = "User"

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)  # 将作为参数传入的属性根据 = 两边保存到实例属性中，即将uid = 12345保存到 self
            # self.name = value  # 不适用 self.name 的原因是，这里的 self.name 不是指给传入的参数赋予 = 右边的值，而是直接给 name 这个属性赋值

    def save(self):
        fields = []
        args = []
        for k, v in User.__mappings__.items():
            fields.append(v[0])  # 这里是获取实际上用于 MYSQL 语句的表头，即 name = ('username', "varchar(30)") 中的 'username'
            args.append(getattr(self, k, None))  # 这里是根据上边 setattr 设置了实例属性后，通过将 __mappings__ 的 key 传入到 self 中，读取到 key 对应的在 self 的值，如 uid的值12345

        sql = 'insert into {} ({}) values ({})'.format(User.__table__, ','.join(fields), ','.join([str(i) for i in args]))  # 最终显示结果 insert into User (uid,username,email,password) values (12345,Michael,test@orm.org,my-pwd)
        print('SQL: {}'.format(sql))


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
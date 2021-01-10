class ModelMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        mappings = dict()

        for k, v in attrs.items():

            if isinstance(v, tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
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
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []
        for k, v in User.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        args_temp = []
        for temp in args:
            if isinstance(temp, int):
                args_temp.append(str(temp))
            if isinstance(temp, str):
                args_temp.append("'{}'".format(temp))

        sql = 'insert into {} ({}) values ({})'.format(User.__table__, ','.join(fields), ','.join([str(i) for i in args_temp]))
        # 最终显示结果 insert into User (uid,username,email,password) values (12345,'Michael','test@orm.org','my-pwd')
        print('SQL: {}'.format(sql))


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
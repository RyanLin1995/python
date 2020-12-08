class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("{} 来了".format(self.name))

    def __del__(self):

        print("{} 我去了".format(self.name))


# Tom是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del关键字可以删除一个对象
del tom

print("-" * 50)
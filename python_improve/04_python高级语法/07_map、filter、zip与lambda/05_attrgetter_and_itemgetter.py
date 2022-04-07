from operator import attrgetter, itemgetter


class user(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        """面向交互式的显示，更底层"""
        return self.name + ":" + str(self.age)

    def __str__(self):
        """更加友好的显示"""
        return self.name + ":" + str(self.age) + ":" + self.gender

    def __call__(self):
        return [self.name, self.age, self.gender]


# 如果同时设置了 __repr__ 与 __str__，print 会显示 __str__，终端会显示 __repr__
a = user("Mike", 29, "B")
b = user("Lily", 28, "B")
c = user("Tom", 28, "A")
d = user("Ben", 23, "B")

users = [a, b, c, d]
print("原始数据：")
for i in users:
    print(i)

print("排序后：")
print("Attrgetter:")
# attrgetter 根据元组的某个字段（key）给元组列表排序
print(sorted(users, key=attrgetter("age", "gender")))

print("Itemgetter:")
users = [user("Mike", 29, "B").__call__(), user("Lily", 28, "B").__call__(),
         user("Tom", 28, "A").__call__(), user("Ben", 23, "B").__call__()]
# itemgetter 根据元组的某个字段（index）给元组列表排序
print(sorted(users, key=itemgetter(1, 2)))  # 按照第一个元素（age）和第二个元素（gender）排序

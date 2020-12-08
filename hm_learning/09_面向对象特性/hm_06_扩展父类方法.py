class Animal:

    def eat(self):
        print('吃---')

    def drink(self):
        print('喝---')

    def run(self):
        print('跑---')

    def sleep(self):
        print('睡---')


class Dog(Animal):

    def bark(self):
        print('汪汪叫')


class Xiaotianquan(Dog):

    def fly(self):
        print('我会飞')

    def bark(self):

        # 1. 针对子类特有需要求,编写代码
        print("叫的跟神一样...")

        # 2. 使用super(). 调用原本在父类中封装的方法
        # super().bark()

        # 使用父类名.方法(self)
        # Dog.bark(self)
        # 注意: 如果使用子类调用方法,可能出现死循环
        # Xiaotianquan.bark(self)

        # 3. 增加其他子类的代码
        print("@#$@$%^%@^&")


xtq = Xiaotianquan()

# 如果子类中,重写了父类的方法
# 在使用子类对象调用方法时,会调用子类中重写的方法
xtq.bark()

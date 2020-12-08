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


# 创建一个哮天犬对象
xtq = Xiaotianquan()

xtq.fly()
xtq.bark()
xtq.eat()

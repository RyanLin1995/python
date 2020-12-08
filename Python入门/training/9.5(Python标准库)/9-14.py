from random import randint

class Die():
    """这是一个模拟骰子的类"""
    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):
        x = randint(1,self.sides)
        print(x)

test_1 = Die(6)
for i in range(1,11):
    test_1.roll_die()

print('\n')

test_2 = Die(10)
for j in range(1,11):
    test_2.roll_die()

print('\n')

test_3 = Die(20)
for k in range(1,11):
    test_3.roll_die()

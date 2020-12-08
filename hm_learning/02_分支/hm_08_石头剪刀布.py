import random

# 1. 从控制台输入要出的拳--石头（1）/剪刀（2）/布（3） 同时做出限制
try:
    user = int(input("请输入您要出的拳 石头（1）/剪刀（2）/布（3）"))
except ValueError:
    print('请输入数字')
# 2. 电脑随机出拳--先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1, 3)


# 3. 定义出拳类型
def finger_guessing_usertype():
    if user == 1:
        print('你出的拳是石头')
    elif user == 2:
        print('你出的拳是剪刀')
    else:
        print('你出的拳是布')


def finger_guessing_computertype():
    if computer == 1:
        print('电脑出的拳是石头')
    elif computer == 2:
        print('电脑出的拳是剪刀')
    else:
        print('电脑出的拳是布')


# 4. 比较胜负
try:
    if user > 3:
        print('请输入数字1-3')
    else:
        if (user == 1 and computer == 2) or (user == 2 and computer == 3) or \
                (user == 3 and computer == 1):
            finger_guessing_usertype()
            finger_guessing_computertype()
            print('恭喜，你赢了')
        elif user == computer:
            finger_guessing_usertype()
            finger_guessing_computertype()
            print('打平了，请再来一局')
        else:
            finger_guessing_usertype()
            finger_guessing_computertype()
            print('很遗憾，你输了')
except NameError:
    pass

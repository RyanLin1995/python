# 使用枚举量代替字面量
from enum import Enum

# 用户每日奖励积分数量
DAILY_POINTS_REWARDS = 100
# VIP 用户每日额外奖励积分数量
VIP_EXTRA_POINTS = 20


# 在定义枚举类型的时候，如果同时继承一些基础类型，例如 int、str,
# 枚举类型就能同时充当该基础类型使用。比如这里的 UserType 就可以当 int 使用。
class UserType(int, Enum):
    # VIP 用户
    VIP = 3
    # 小黑屋用户
    BANNED = 13


class User:
    def __init__(self, user_type, points):
        self.type = user_type

        if not isinstance(points, int):
            raise TypeError("points must be an integer")
        elif points < 0:
            raise ValueError("points must be greater than 0")
        elif points != 0:
            self.points = points
        else:
            self.points = 0


def add_daily_points(user):
    """
    用户每天完成第一次登录后，为其增加积分
    """
    # if user.type == 13:
    #     return
    # if user.type == 3:
    #     user.points += 120
    #     return
    # user.points += 100
    # return

    # 枚举量代替字面量
    if user.type == UserType.BANNED:
        return
    if user.type == UserType.VIP:
        user.points += DAILY_POINTS_REWARDS + VIP_EXTRA_POINTS
        return

    user.points += DAILY_POINTS_REWARDS
    return


if __name__ == "__main__":
    user = User(3, 123)
    add_daily_points(user)
    print(user.points)

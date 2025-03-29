class UserCollectionWithoutLen:

    def __init__(self, users):
        self.items = users


class UserCollection:

    def __init__(self, users):
        self.items = users

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    users_without_len = UserCollectionWithoutLen([])
    # 不实现 __len__() 方法情况下，对对象进行判断时，无法使用“真值测试”
    # 真值测试：计算出布尔值进行比较
    if users_without_len:
        print(users_without_len)

    blank_users = UserCollection([])
    if blank_users:  # 实现 __len__() 方法后，对对象进行判断时，可以正常使用“真值测试”
        print("blank users")

    not_blank_users = UserCollection(["ryan", "lancy", "suki", "gigi", "admin"])
    if not_blank_users:
        print("not blank users")

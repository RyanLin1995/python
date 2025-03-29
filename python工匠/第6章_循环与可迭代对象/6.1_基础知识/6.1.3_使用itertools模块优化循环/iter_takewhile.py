from itertools import takewhile

users = [
    {"username": "jane", "is_active": False},
    {"username": "john", "is_active": True},
    {"username": "jim", "is_active": True},
    {"username": "jill", "is_active": False},
]

for user in users:
    if user["is_active"]:
        break
    else:
        print(user["username"])

# 使用 takewhile 替代 break 语句
for user in takewhile(lambda u: not u["is_active"], users):
    print(user["username"])

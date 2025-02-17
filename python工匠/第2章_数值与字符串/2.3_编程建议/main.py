# 1. 使用特殊数字无穷大
def sort_users_inf(users):

    def key_func(username):
        age = users[username]
        # 当年龄为空的时候，返回无穷大作为 key，因此会被排到最后
        return age if age else float("inf")

    return sorted(users, key=key_func)


users = {
    "alice": 25,
    "dan": 40,
    "bob": 30,
    "charlie": None,
    "elizabeth": 35,
}
print(sort_users_inf(users))


# 2. 别忘了以 r 开头的字符串内置方法
log_line = (
    '"AppleWebkit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" 47632'
)
print(log_line.rsplit(maxsplit=1))  # 从右向左分割字符串，最多分割一次


# 3. 多级缩进里出现多行字符串
print(
    """Welcome, today's movie list:
    - Jaw (1975)
    - The Shinning (1980)
    - Saw (2024)
    """
)

from textwrap import dedent

print(
    dedent(
        """
    Welcome, today's movie list:
    - Jaw (1975)
    - The Shinning (1980)
    - Saw (2024)
    """
    )
)  # dedent 函数可以自动去除缩进

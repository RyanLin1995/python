import re


def main(password):
    """确保传入的口令字符为强口令
    要求: 长度不少于8位，同时包括大小写，至少有一位数字"""
    passRegex = re.compile(r"[A-Z]+")
    passRegex1 = re.compile(r"[a-z]+")
    passRegex2 = re.compile(r"[0-9]+")
    passRegex3 = re.compile(r"\w{8,}")
    ret = passRegex.search(password)
    ret1 = passRegex1.search(password)
    ret2 = passRegex2.search(password)
    ret3 = passRegex3.search(password)
    if ret and ret1 and ret2 and ret3:
        print('是强口令')
    else:
        print('不是强口令')


if __name__ == '__main__':
    main('1A2B3c4d5t')
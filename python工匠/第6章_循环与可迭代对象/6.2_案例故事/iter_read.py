# -*- coding: utf-8 -*-


# 这个函数有个问题，当读取的文件超过5GB之后，读取的时间会很长，占用的内存会增加。
def count_digits(fname):
    """计算文件里包含多少个数字字符"""
    count = 0
    with open(fname) as file:
        for line in file:
            for s in line:
                if s.isdigit():
                    count += 1
    return count


# -------------------------------------------------------------------------------------------
# 优化版本，每次读取 8kb，加速了读取速度，同时也降低了内存占用。
def count_digits_v2(fname):
    """计算文件里包含多少个数字字符，每次读取 8kb"""
    count = 0
    block_size = 1024 * 8
    with open(fname) as file:
        while True:
            chunk = file.read(block_size)
            # 当文件没有更多内容时，read 调用将会返回空字符串 ''
            if not chunk:
                break
            for s in chunk:
                if s.isdigit():
                    count += 1
    return count


# -------------------------------------------------------------------------------------------
from functools import partial


# 优化了 v2 版本，使用 partial 构造了一个无需参数的函数，
# 然后利用 iter 构造一个迭代器，每次迭代都会调用这个函数。
def count_digits_v3(fname):
    count = 0
    block_size = 1024 * 8
    with open(fname) as fp:
        # 使用 functools.partial 构造一个新的无需参数的函数
        _read = partial(fp.read, block_size)

        # 利用 iter() 构造一个不断调用 _read 的迭代器
        for chunk in iter(_read, ""):
            for s in chunk:
                if s.isdigit():
                    count += 1
    return count


# -------------------------------------------------------------------------------------------


# 新的需求，当需要统计所有偶数的时候，应该按职责拆解循环体代码
def read_file_digits(fp, block_size=1024 * 8):
    """生成器函数：分块读取文件内容，返回其中的数字字符"""
    _read = partial(fp.read, block_size)
    for chunk in iter(_read, ""):
        for s in chunk:
            if s.isdigit():
                yield s


def count_digits_v4(fname):
    count = 0
    with open(fname) as file:
        for num in read_file_digits(file):
            count += 1
    return count


from collections import defaultdict


def count_even_groups(fname):
    """分别统计文件里每个偶数字符出现的个数"""
    counter = defaultdict(int)
    with open(fname) as file:
        for num in read_file_digits(file):
            if int(num) % 2 == 0:
                counter[int(num)] += 1
    return counter


print(count_digits("small_file.txt"))
print(count_digits_v2("small_file.txt"))
print(count_digits_v3("small_file.txt"))
print(count_digits_v4("small_file.txt"))
print(count_even_groups("small_file.txt"))

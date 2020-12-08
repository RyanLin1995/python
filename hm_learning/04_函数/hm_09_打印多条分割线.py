def print_line(char, times):

    print(char * times)


def print_lins(char, times):
    """打印多条分割线

    :param char: 分割线类型
    :param times: 次数
    """
    row = 0

    while row < 5:

        print_line(char, times)

        row += 1


print_lins('-', 10)
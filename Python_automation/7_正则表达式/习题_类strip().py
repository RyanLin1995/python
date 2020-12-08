import re


def main(string1, string2):
    """根据字符串2的要求，去除字符串1中的值
    如果没有传入值，则从最后开始去除"""
    strRegex = re.compile(string2)
    ret = strRegex.match(string1)
    print(ret.group())


if __name__ == '__main__':
    main('napplen', 'n')
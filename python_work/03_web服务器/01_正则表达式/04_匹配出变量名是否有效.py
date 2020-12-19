import re


def main():
    names = ['name1', '_name', '2_name', '__name__', 'name2me', 'n_ame', 'name!', 'name#123']

    for name in names:
        ret = re.match(r'^[_a-zA-Z][a-zA-Z0-9_]*$', name)  # 在正则表达式中判断开头，使用
        # ^, 判断结尾，使用 $。 match方法自带判断开头

        if ret:
            print("变量名 {} 符合要求".format(ret.group()))

        else:
            print("变量名 {} 不符合要求".format(name))


if __name__ == '__main__':
    main()

# 要匹配的项为 GET /index.html HTTP/1.1
# ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])  # [^/]+ 表示匹配不是 / 的所有内容
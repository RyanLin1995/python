# 需求：匹配出163的邮箱地址，且@符号钱有4到20位，例如hello@163.com
import re


def main():

    mailAddres = ['laowang@163Acom','__@163.com', 'ABCD@163.com', '1@163.com', '56364504@qq.com', 'hello@163.com', 'helloworld@163.com', 'helloworldhelloworldhelloworld@163.com']

    for mailAddre in mailAddres:
        # 因为 . 在正则中是有意义的，因此需要转义
        ret = re.match(r'^[a-zA-Z0-9]{4,20}@163\.com$', mailAddre)

        if ret:
            print("邮箱 {} 正确， 正确的位数为 {}".format(mailAddre, ret.group()))
        else:
            print("邮箱 {} 不正确".format(mailAddre))


if __name__ == '__main__':
    main()
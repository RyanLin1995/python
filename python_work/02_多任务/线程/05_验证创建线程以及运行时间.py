import time
import threading


# 如果创建target时创建的函数结束了，那么意味着这个子线程结束了
def test1():
    for i in range(5):
        print("----test1----{}".format(i))
        time.sleep(1)


def main():
    # 在调用Thread之前先打印当前线程信息
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)

    # 在调用Thread之后打印
    print(threading.enumerate())
    t1.start()

    # 在调用start之后打印
    print(threading.enumerate())


if __name__ == '__main__':
    main()
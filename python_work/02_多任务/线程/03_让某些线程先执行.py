import time
import threading


def test1():
    for i in range(5):
        print("----test1----{}".format(i))


def test2():
    for i in range(5):
        print("----test2----{}".format(i))


def main():

    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)
    print("----1----")

    t2.start()
    time.sleep(1)
    print("----2----")

    print(threading.enumerate())


if __name__ == '__main__':
    main()
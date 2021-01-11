import time
import greenlet


def test1():
    while True:
        print("---A---")
        g2.switch()
        time.sleep(0.1)


def test2():
    while True:
        print("---B---")
        g1.switch()
        time.sleep(0.1)


if __name__ == '__main__':
    g1 = greenlet.greenlet(test1)
    g2 = greenlet.greenlet(test2)
    # 切换到g1
    g1.switch()
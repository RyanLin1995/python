import threading
import time


def test1(temp, num_list2):

    temp.append(33)
    num_list2 = temp[:]
    num_list2 += num_list2

    print("test1 list: {} and {}".format(temp, num_list2))

    return num_list2


def test2(temp, temp2):

    print("test2 list: {} and {}".format(temp, temp2))


num_list = [11, 22]
num_list2 = []


def main():

    t1 = threading.Thread(target=test1, args=(num_list, num_list2))

    t2 = threading.Thread(target=test2, args=(num_list, num_list2))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("Global list: {} and {}".format(num_list, num_list2))


if __name__ == '__main__':
    main()
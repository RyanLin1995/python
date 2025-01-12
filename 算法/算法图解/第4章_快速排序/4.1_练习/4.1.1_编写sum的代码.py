import time


def sum_test(arr):
    # 递归计算数组中所有元素的和
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_test(arr[1:])


if __name__ == '__main__':
    test_arr = list(range(1, 999))
    start = time.perf_counter()
    print(sum_test(test_arr))
    end = time.perf_counter()
    print(end - start)

    start = time.perf_counter()
    print(sum(test_arr))
    end = time.perf_counter()
    print(end - start)

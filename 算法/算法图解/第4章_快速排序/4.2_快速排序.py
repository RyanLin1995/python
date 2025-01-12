import random


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    import time

    sort_list = [random.randint(1, 10000) for i in range(9000)]

    start = time.perf_counter()
    quicksort(sort_list)
    print(time.perf_counter() - start)

    start = time.perf_counter()
    sorted(sort_list)
    print(time.perf_counter() - start)

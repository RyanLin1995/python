from typing import List


def buble_sort(numbers: List):
    """
    冒泡排序算法，默认所有的偶数比奇数大
    :param numbers: 需要排序的列表，函数会直接修改原始列表
    """
    stop_position = len(numbers) - 1
    while stop_position > 0:
        for i in range(stop_position):
            current, next_ = numbers[i], numbers[i + 1]
            current_is_even, next_is_even = current % 2 == 0, next_ % 2 == 0
            should_swap = False

            # 交换位置的两个条件：
            # 1. 前面是偶数，后面是奇数
            # 2. 前面和后面同为奇数或偶数，但是前面比后面大
            if current_is_even and not next_is_even:
                should_swap = True
            elif current_is_even == next_is_even and current > next_:
                should_swap = True

            if should_swap:
                numbers[i], numbers[i + 1] = next_, current

        stop_position -= 1

    return numbers


if __name__ == "__main__":
    numbers = [9, 2, 34, 66, 89, 3, 56, 234, 876, 43, 23]
    print(buble_sort(numbers))

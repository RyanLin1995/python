# 二分查找法：一种高效的查找算法，适用于在一个有序数组中查找特定元素。其基本原理是通过反复将查找范围缩小一半，从而快速定位目标元素。

def binary_search(arr, target):
    low = 0  # 初始化查找范围
    high = len(arr) - 1  # 初始化查找范围

    while low <= high:
        mid = (low + high) // 2  # 计算中间位置
        guess = arr[mid]  # 获取中间元素
        # 比较中间元素：
        # 如果中间元素等于目标值，则查找成功，返回中间位置的索引。
        # 如果中间元素小于目标值，则目标值位于右半部分，更新
        # low 为 mid + 1。
        # 如果中间元素大于目标值，则目标值位于左半部分，更新
        # high 为 mid - 1。
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    print(binary_search(arr, 3))
    print(binary_search(arr, -1))

def count_element(arr):
    """
    使用递归计算列表包含的元素个数
    """
    if not arr:  # 基准条件：如果列表为空
        return 0
    else:
        return 1 + count_element(arr[1:])


if __name__ == '__main__':
    print(count_element([1, 2, 3, 4, 5, 6]))

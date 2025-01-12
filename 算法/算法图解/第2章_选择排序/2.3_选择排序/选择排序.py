# 运行时间：O(n²)

def findSmallest(arr):
    smallest = arr[0]  # 默认最小值
    smallest_index = 0  # 最小值索引

    for i in range(1, len(arr)):
        if arr[i] < smallest:  # 如果当前元素小于最小值，则更新最小值和最小值索引。
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):  # 选择排序
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # 找到最小值
        newArr.append(arr.pop(smallest))  # 将最小值添加到新数组中，并从原数组中删除
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))

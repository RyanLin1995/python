prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来。比如，下面是查找最小和最大股票价格和股票值的代码
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 类似的，可以使用 zip() 和 sorted() 函数来排列字典数据
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# 需要注意的是在计算操作中使用到了(值，键)对。当多个实体拥有相同的值的时候，键会决定返回结果。
prices = {'AAA': 45.23, 'ZZZ': 45.23}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))

from itertools import permutations, combinations, combinations_with_replacement

items = ['a', 'b', 'c']
for p in permutations(items):  # 接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成
    print(p)

print("\n")

for p in permutations(items, 2):  # 参数 r 可以指定返回的长度
    print(p)

print("\n")

for p in combinations(items, 3):  # 返回由输入 iterable 中元素组成长度为 r 的子序列。如果元素各自不同，那么每个组合中没有重复元素
    print(p)

print("\n")

for p in combinations_with_replacement(items, 3):  # 返回由输入 iterable 中元素组成的长度为 r 的子序列，允许每个元素可重复出现
    print(p)

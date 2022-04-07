name_list = ["张三", "李四", "王五", "王小二"]

# 使用迭代遍历列表
"""
顺序的从列表中依次获取数据，每一次循环过程中，数据都保存在name这个变量中，
在循环内部可以访问到当前这一次获取到的数据
"""

for name in name_list:
    print('我的名字是%s' % name)

# 带有 index 的列表遍历
print(list(enumerate(name_list)))

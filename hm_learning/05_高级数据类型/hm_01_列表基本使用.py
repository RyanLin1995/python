name_list = ['zhangsan', 'lisi', 'wangwu']

# 1. 取值和取索引
# 取值
print(name_list[0])
# 取索引（知道数据内容，想知道数据在列表中的位置）
print(name_list.index('lisi'))

# 2. 修改
name_list[1] = '李四'

# 3. 增加
# 在列表索引处追加数据
name_list.insert(0, 'liuliu')
# 在列表末尾追加数据
name_list.append('小明')
# 将一个列表追加到另一个列表
name_list_2 = ['孙悟空', '猪八戒', '沙僧']
name_list.extend(name_list_2)

# 4. 删除
# 删除列表中某一个数据
name_list.remove('liuliu')
# pop默认删除列表最后一项，也可以删除列表中指定索引的参数
name_list.pop()
name_list.pop(0)
# clear方法可以清空列表
name_list.clear()

print(name_list)
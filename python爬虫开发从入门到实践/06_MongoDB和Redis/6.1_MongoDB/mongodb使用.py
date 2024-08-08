from pymongo import MongoClient

client = MongoClient()

# 1. 初始化数据库
# 数据在 MongoDB 中是按照 "库( Database )" - "集合( Collections )" - "文档( Document)" 的层级关系来存储的。
# 如果使用 Python 的数据结构来做类比的话，文档相当于一个字典，集合相当于一个包含了很多字典的列表，库相当于一个大字典，
# 大字典里面的每一个键值对都对应了一个集合，Key为集合的名字，Value 就是一个集合。
database = client['test']
collection = database['spider']

# 2. 插入数据
# 插入单条数据
# data = {'id': 123, 'name': 'ryan', 'age': 20, 'salary': 999}
# collection.insert_one(data)

# 插入多条数据
# more_data = [
#     {'id': 1, 'name': '张三', 'age': 10, 'salary': 0},
#     {'id': 2, 'name': '李四', 'age': 20, 'salary': -100},
#     {'id': 3, 'name': '王五', 'age': 30, 'salary': 1000},
#     {'id': 4, 'name': '外国人', 'age': 40, 'salary': ""}
# ]
# collection.insert_many(more_data)


# 3. 普通查找
# find(查询条件, 返回字段)
# find_one(查询条件, 返回字段)

# # 查找所有信息
# content = [x for x in collection.find()]
# print(content)
#
# # 根据条件查找信息
# content = [x for x in collection.find({'age': 28})]
# print(content)
#
# # 根据条件查找信息并根据返回字段返回信息
# content = [x for x in
#            collection.find({'age': 28}, {'_id': 0, 'name': 1, 'salary': 1})]  # 0 表示不返回该字段，1 表示返回。_id 比较特殊，必须人工指定为 0
# print(content)

# 4. 逻辑查询
# 符号     意义
# $gt     大于
# $lt     小于
# $gte    大于等于
# $lte    小于等于
# $eq     等于
# $ne     不等于
# content = collection.find({'age': {'$gt': 27}}, {'_id': 0, 'name': 1, 'age': 1})  # 查询所有大于 27 岁的记录
# print([x for x in content])
#
# content = collection.find({'age': {'$gt': 27, '$lte': 40}}, {'_id': 0, 'name': 1, 'age': 1})  # 27 < age <= 40 的记录
# print([x for x in content])
#
# content = collection.find({'salary': {'$ne': 29}}, {'_id': 0, 'name': 1, 'age': 1})  # 查询所有 salary 不等于 29 的记录
# print([x for x in content])

# 5. 对查询结果排序
# sort('列名', 1或-1)  1 表示升序 -1 表示降序
# content = collection.find({'age': {'$gt': 27, '$lt': 40}}, {'_id': 0, 'name': 1, 'age': 1}).sort({'age': -1})
# print([x for x in content])

# 6. 更新记录
# update_one(参数1, 参数2)
# update_many(参数1, 参数2)
# 两个语句的参数都是字典，都不能省略。参数1 为寻找需要更新的记录，参数2 为用来更新的记录
# collection.update_one({'age': 20}, {'$set': {'name': 'test'}})
# collection.update_many({'age': 20}, {'$set': {'age': 30}})

# 7. 删除数据
# delete_one(参数)
# delete_many(参数)
# 参数都是字典
# collection.delete_one({'name': 'test'})
# collection.delete_many({'age': 30})

# 8. 对查询结果去重
# distinct('列名')
content = collection.distinct('age')
print([x for x in content])

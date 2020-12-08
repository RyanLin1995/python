xiaoming = {"gl_name": "小明"}

# 1. 取值
print(xiaoming["gl_name"])
# 在取值时，如果指定的key不存在，程序会报错
# print(xiaoming["name123"])

# 2. 增加/修改
# 如果key存在，就修改key的值
# 如果key不存在，就会新增键值对
xiaoming["age"] = 18
xiaoming["gl_name"] = "小王"
# 3. 删除
xiaoming.pop("gl_name")

print(xiaoming)
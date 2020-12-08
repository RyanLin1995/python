xiaoming = {"gl_name": "小明",
            "age": 18}

# 1. 统计键值对数量
print(len(xiaoming))

# 2. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}
# 如果被合并的字典包含已经存在的键值对，会覆盖原来的
xiaoming.update(temp_dict)

# 3. 清空字典
xiaoming.clear()

print(xiaoming)
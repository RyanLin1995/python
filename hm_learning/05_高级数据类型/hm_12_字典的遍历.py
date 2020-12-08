xiaoming = {"gl_name": "小明",
            "qq": 188888888,
            "phone": 19999999}

# 迭代遍历字典
# 变量k是每一次循环中，获取到的键值对的key
for k in xiaoming:
    print("%s - %s" % (k, xiaoming[k]))

for k, v in xiaoming.items():
    print("%s - %s" % (k, v))

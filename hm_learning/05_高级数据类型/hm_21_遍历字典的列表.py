student = [
    {"gl_name": "阿土"},
    {"gl_name": "小美"}
]

# 在学院列表中搜索指定的姓名
find_name = "阿土"

for stu_dict in student:
    print(stu_dict)

    if stu_dict["gl_name"] == find_name:
        print("找到了%s" % find_name)

        # 如果已经找到，应该直接退出．而不再遍历后续元素
        break

else:
    # 如果希望在搜索列表时,所有的字典检查之后,都没有发现需要搜索的目标,还希望得到一个统一的提示
    print("抱歉，没有找到%s" % find_name)

print("循环结束")

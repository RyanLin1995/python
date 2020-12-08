# 使用对个键值对，存储描述一个物体的相关信息，要描述更复杂的数据信息
# 将多个字典放在一个列表中，再进行遍历

card_list = [
    {"gl_name": "zhangsan",
     "qq": "12345",
     "phone": 110},
    {"gl_name": "lisi",
     "qq": "54321",
     "phone": 10086},
]

for card_info in card_list:
    print(card_info)
    # for k, v in card_info.items():
    #     print(type(v))


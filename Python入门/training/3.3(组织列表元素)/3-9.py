#coding:gbk
#想要请谁参加晚餐
invite_name=["Feizai" , "AHao" , "Zhezhe" , "QianLan"]
message="Hi" + " " + invite_name[0] + "," + invite_name[1] + "," + \
        invite_name[2] + " " + "and" + " " + invite_name[3] + "," + \
        'I want to invite you to dinner.'
print(message)

#指出谁无法赴约
message=invite_name[3] + " " + "can't come to the dinner because of the work."
print(message)

#替换嘉宾名单
invite_name[3]="Siyuan"
message="I will invite" + " " + invite_name[3] + " " + "to the dinner."
print(message)

#找到更加大的餐厅
print("Hi All,I found a bigger shop")

#增加一位嘉宾到开头
#增加一位到中间
#增加一位到结尾
invite_name.insert(0,"Xueting")
invite_name.insert(2,"Ajuan")
invite_name.append("Aqiao")
message="Hi" + " " + invite_name[0] + "," + invite_name[1] + "," + \
        invite_name[2] + "," + invite_name[3] + " " + invite_name[4] + " " + \
        invite_name[5] + " " + "and" + " " + invite_name[6] + " " + \
        "I want to invite you to dinner."
print(message)

print(invite_name)

#位置不够，去掉其他，只保留一位
print("I am sorry that I only invite two people")

invite_name_pop_1=invite_name.pop(0)
message_1="I am sorry" + "," + invite_name_pop_1 + "."
print(message_1)

invite_name_pop_2=invite_name.pop(0)
message_2="I am sorry" + "," + invite_name_pop_2 + "."
print(message_2)

invite_name_pop_3=invite_name.pop(0)
message_3="I am sorry" + "," + invite_name_pop_3 + "."
print(message_3)

invite_name_pop_4=invite_name.pop(0)
message_4="I am sorry" + "," + invite_name_pop_4 + "."
print(message_4)

invite_name_pop_5=invite_name.pop()
message_5="I am sorry" + "," + invite_name_pop_5 + "."
print(message_5)

invite_name_pop_6=invite_name.pop()
message_6="I am sorry" + "," + invite_name_pop_6 + "."
print(message_6)

print(invite_name)
#用len查看最终要请人数
print(len(invite_name))

del invite_name[0]
print(invite_name)



# 定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True
# 定义整数型变量 knife_length 表示刀的长度，单位：厘米
knife_length = 21
# 首先检查是否有车票，如果有，才允许进行安检
if has_ticket:
    print('安检通过')
# 安检时，需要检查刀的长度，判断是否超过20厘米
    if knife_length > 20:
# 如果超过20厘米，提示刀的长度过长，不允许上车
        print('刀过长，长达%d厘米,不准上车' % knife_length)
# 如果不超过20厘米，安检通过
    else:
        print('没有违禁品，允许上车')
# 如果没有车票，不允许进入候车室
else:
    print('请先买票')
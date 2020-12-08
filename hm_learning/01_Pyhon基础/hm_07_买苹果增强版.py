# 1.输入苹果的单价
price_str = input('苹果的价格：')

# 2.输入苹果的重量
weight_str = input('苹果的重量：')

# 3.计算支付的金额
price = float(price_str)
weight = float(weight_str)
money = price * weight

print(money)
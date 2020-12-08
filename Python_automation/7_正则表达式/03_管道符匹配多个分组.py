import re

# 1. 匹配多个表达式中的一个
# 匹配许多表达式中的一个时，可以使用管道符|
# 注意，当被搜索对象有两个或以上匹配时，将会显示先匹配的文本
heroRegex = re.compile(r"Batman|Tina Fey")
mo1 = heroRegex.search("Batman and Tina Fey")
print(mo1.group())

mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())


# 2. 匹配多个模式中的一个
# 例如要在文本中搜索Batman, Batmobile, Batcopter, Batbat中的一个
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search("Batman is driving the Batmobile")
print(mo.group())  # 返回完整匹配文本
print(mo.group(0))  # 返回完整匹配文本
print(mo.group(1))  # 返回分组1

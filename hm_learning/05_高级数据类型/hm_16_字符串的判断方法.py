# 1. 判断空的字符串
space_str = "    \t\n\r"

print(space_str.isspace())

# 2. 判断字符串中是否包含数字
# 下边方法都不能判断小数
num_str = "一千零一"

print(num_str)
print(num_str.isdecimal())  # 只能判断单纯数字
print(num_str.isdigit())  # 可以判断unicode
print(num_str.isnumeric())  # 可以判断上边两个和汉语数字

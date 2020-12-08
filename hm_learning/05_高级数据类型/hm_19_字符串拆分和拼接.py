# 假设: 以下内容是从网络上抓取的
# 要求:
# 1.将空白字符串去掉
# 2.再使用" "作为分隔符,拼接成为一个整齐的字符串
poem_str = "登鹳雀楼\t\n王之涣\t\n白日依山尽\t\t  黄河入海流\t\t 欲穷千里目\t更上一层楼"

print(poem_str)

# 1. 拆分字符串
poem = poem_str.split()
print(poem)

# 2. 合并字符串
# result = " ".join(poem)
# print(result)

for i in poem:
    print(i.center(10, "　"))

import time


# 计算函数运行时间
def calc_prod():

    procudt = 1
    for i in range(1, 100000):
        procudt = procudt * i
    return procudt


start = time.time()  # time.time() 返回的是浮点数
prod = calc_prod()
end = time.time()

print(f"The result len is : {len(str(prod))} and run {end - start} seconds")

# 阻塞程序运行
for i in range(3):
    print("Tick")
    time.sleep(1)
    print("Tock")
    time.sleep(1)

# 四舍五入
# python 可以使用 round 进行小数的四舍五入，第一个参数是数字，第二个参数是保留的位数
# now = time.time()
# while True:
#     print(round(now, 2))


# 扩展：生成时间戳
dt = "18:15:21 Oct 12, 2019"
date_array = time.strptime(dt, "%H:%M:%S %b %d, %Y")  # time.strptime 返回 struct_time
print(time.mktime(date_array))  # 参数是 struct_time，返回时间戳
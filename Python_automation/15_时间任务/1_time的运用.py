import time


# 一 计算函数运行时间
def calc_prod():

    procudt = 1
    for i in range(1, 100000):
        procudt = procudt * i
    return procudt


start = time.time()  # time.time() 返回的是浮点数
prod = calc_prod()
end = time.time()

print(f"The result len is : {len(str(prod))} and run {end - start} seconds")

# 二 阻塞程序运行
for i in range(3):
    print("Tick")
    time.sleep(1)
    print("Tock")
    time.sleep(1)

# 三 四舍五入
# python 可以使用 round 进行小数的四舍五入，第一个参数是数字，第二个参数是保留的位数
now = time.time()
while True:
    print(round(now, 2))
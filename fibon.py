# 斐波那契数列
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for i in fibon(100):
    print(f'\b' * i, end='', flush=True)  # 擦除屏幕当前行末尾的字符
    print(i, end='', flush=True)

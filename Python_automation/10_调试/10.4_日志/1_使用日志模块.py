import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y%m%d", filename="log.txt")

# logging.disable(logging.CRITICAL)  #停止日志调用


# 设计一个数的阶乘函数
def factorial(n):
    logging.debug("Start a program")
    total = 1
    # for i in range(n + 1):  # 函数从0开始，但是任何数字乘以0都得0
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is {}, total is {}".format(i, total))
    return total


print(factorial(5))
logging.debug("End of program")

# 常用格式
# % (levelno)s: 打印日志级别的数值
# % (levelname)s: 打印日志级别名称
# % (pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
# % (filename)s: 打印当前执行程序名
# % (funcName)s: 打印日志的当前函数
# % (lineno)d: 打印日志的当前行号
# % (asctime)s: 打印日志的时间
# % (thread)d: 打印线程ID
# % (threadName)s: 打印线程名称
# % (process)d: 打印进程ID
# % (message)s: 打印日志信息
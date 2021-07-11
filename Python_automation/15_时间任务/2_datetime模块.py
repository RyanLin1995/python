import time
import datetime

# 打印当前时间
print(datetime.datetime.now())

# 获取特定日期的 datatime 对象
dt = datetime.datetime(2021, 7, 4, 16, 0, 0)
print(f"Year: {dt.year}")
print(f"Month: {dt.month}")
print(f"Day: {dt.day}")
print(f"Hour: {dt.hour}")
print(f"Min: {dt.minute}")
print(f"Second: {dt.second}")

# 转换时间戳
print(datetime.datetime.fromtimestamp(time.time()))

# 比较时间大小
now = datetime.datetime.now()
yesterday = datetime.datetime(2021, 7, 10, 17, 32)
print(yesterday < now)

import time
import datetime

# 打印当前时间
print(datetime.datetime.now())  # 返回的是 time.time() 的浮点数然后再加上格式
#############################

# 获取特定日期的 datatime 对象
dt = datetime.datetime(2021, 7, 4, 16, 0, 0)
print(dt)
print(f"Year: {dt.year}")
print(f"Month: {dt.month}")
print(f"Day: {dt.day}")
print(f"Hour: {dt.hour}")
print(f"Min: {dt.minute}")
print(f"Second: {dt.second}")
#############################

# 转换时间戳
print(datetime.datetime.fromtimestamp(time.time()))  # 等价于 datetime.datetime.today()
#############################

# 比较时间大小
now = datetime.datetime.now()
yesterday = datetime.datetime(2021, 7, 10, 17, 32)
print(yesterday < now)
#############################

# timedelta 函数：生成一个时间段
# timedelta 生成一个时间段，接受weeks,days,hours,minutes,seconds,milliseconds 跟 microseconds 参数，返回的总时间以天，秒，微秒表示
delta = datetime.timedelta(days=50, hours=10, minutes=10, seconds=10)
print(delta)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())  # 总秒数

# timedelta 函数返回的值可以使用算术运算符进行计算
now = datetime.datetime.now()
dt = datetime.timedelta(days=1000)
print(now + dt)  # 计算当前时 + 1000天后的时间
about_ten_years_ago = datetime.timedelta(days=365 * 10)
print(now - about_ten_years_ago)  # 计算十年前的今天
print(now - 2 * about_ten_years_ago)  # 计算二十年前的今天

# strftime 函数： 将 datetime 对象转为字符串
# strftime 参数       含义
# %Y                 带世纪的年份，例如'2014'
# %y                 不带世纪的年份，'00'至'99'（1970 至 2069）
# %m                 数字表示的月份, '01'至'12'
# %B                 完整的月份，例如'November'
# %b                 简写的月份，例如'Nov'
# %d                 一月中的第几天，'01'至'31'
# %j                 一年中的第几天，'001'至'366'
# %w                 一周中的第几天，'0'（周日）至'6'（周六）
# %A                 完整的周几，例如'Monday'
# %a                 简写的周几，例如'Mon'
# %H                 小时（24 小时时钟），'00'至'23'
# %I                 小时（12 小时时钟），'01'至'12'
# %M                 分，'00'至'59'
# %S                 秒，'00'至'59'
# %p                 'AM'或'PM'
# %%                 就是'%'字符

old = datetime.datetime(2015, 6, 18, 12, 13, 15)
now = datetime.datetime.now()
print(now.strftime("%Y/%m/%d %H:%M:%S"))
print(old.strftime("%b %d, %Y"))

# strptime 函数： 将字符串转为 datetime 对象
date = "18:15:21 Oct 12, 2019"
date_array = datetime.datetime.strptime(date, "%H:%M:%S %b %d, %Y")
print(date_array)

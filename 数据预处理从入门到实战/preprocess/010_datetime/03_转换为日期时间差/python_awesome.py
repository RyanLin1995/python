import pandas as pd
from preprocess.load_data.data_loader import load_hotel_reserve

customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 将reserve_datetime转换为datetime64[ns]类型
reserve_tb['reserve_datetime'] = pd.to_datetime(reserve_tb['reserve_datetime'], format='%Y-%m-%d %H:%M:%S')

# 将checkin_datetime转换为datetime64[ns]类型
reserve_tb['checkin_datetime'] = pd.to_datetime(reserve_tb['checkin_date'] + reserve_tb['checkin_time'],
                                                format='%Y-%m-%d%H:%M:%S')

# 计算年份差(不考虑月及其以后的日期时间元素)
print(reserve_tb['reserve_datetime'].dt.year - reserve_tb['checkin_datetime'].dt.year)

# 获取月份差(不考虑天及其以后的日期时间元素)
(reserve_tb['reserve_datetime'].dt.year * 12 + reserve_tb['reserve_datetime'].dt.month) - (
        reserve_tb['checkin_datetime'].dt.year * 12 + reserve_tb['checkin_datetime'].dt.month)

# 以天为单位计算差值
reserve_tb['diff_days'] = (reserve_tb['reserve_datetime'] - reserve_tb['checkin_datetime']).dt.days

# 以时为单位计算差值
reserve_tb['diff_hours'] = (reserve_tb['reserve_datetime'] - reserve_tb['checkin_datetime']) / pd.Timedelta(hours=1)

# 以分为单位计算差值
reserve_tb['diff_minutes'] = (reserve_tb['reserve_datetime'] - reserve_tb['checkin_datetime']) / pd.Timedelta(minutes=1)

# 以秒为单位计算差值
reserve_tb['diff_seconds'] = (reserve_tb['reserve_datetime'] - reserve_tb['checkin_datetime']) / pd.Timedelta(seconds=1)

# 打印结果
print(reserve_tb[['diff_days', 'diff_hours', 'diff_minutes', 'diff_seconds']])

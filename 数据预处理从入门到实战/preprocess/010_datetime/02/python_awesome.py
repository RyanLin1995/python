import pandas as pd
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 将reserve_datetime转换为datetime64[ns]类型
reserve_tb['reserve_datetime'] = \
  pd.to_datetime(reserve_tb['reserve_datetime'], format='%Y-%m-%d %H:%M:%S')

# 获取年份
reserve_tb['reserve_datetime'].dt.year

# 获取月份
reserve_tb['reserve_datetime'].dt.month

# 获取日期
reserve_tb['reserve_datetime'].dt.day

# 以数值形式获取星期（0=星期日，1＝星期一）
reserve_tb['reserve_datetime'].dt.dayofweek

# 获取时间中的时
reserve_tb['reserve_datetime'].dt.hour

# 获取时间中的分
reserve_tb['reserve_datetime'].dt.minute

# 获取时间中的秒
reserve_tb['reserve_datetime'].dt.second

# 转换为指定格式的字符串
reserve_tb['reserve_datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
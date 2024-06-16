import pandas as pd
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 通过to_datetime函数转换为datetime64[ns]类型
pd.to_datetime(reserve_tb['reserve_datetime'], format='%Y-%m-%d %H:%M:%S')
pd.to_datetime(reserve_tb['checkin_date'] + reserve_tb['checkin_time'],
               format='%Y-%m-%d%H:%M:%S')

# 从datetime64[ns]类型获取日期信息
pd.to_datetime(reserve_tb['reserve_datetime'],
               format='%Y-%m-%d %H:%M:%S').dt.date
pd.to_datetime(reserve_tb['checkin_date'], format='%Y-%m-%d').dt.date

import pandas as pd
from preprocess.load_data.data_loader import load_hotel_reserve, load_holiday_mst
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()
holiday_mst = load_holiday_mst()

# 本书刊登内容如下
# 与休息日主数据连接
pd.merge(reserve_tb, holiday_mst,
         left_on='checkin_date', right_on='target_day')

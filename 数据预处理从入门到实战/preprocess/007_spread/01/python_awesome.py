import pandas as pd
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 用pivot_table同时实现横向显示和聚合处理
# 向aggfunc参数指定用于计算预订次数的函数
pd.pivot_table(reserve_tb, index='customer_id', columns='people_num',
               values='reserve_id',
               aggfunc=lambda x: len(x), fill_value=0)
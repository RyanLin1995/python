from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 对reserve_tb和hotel_tb以hotel_id为键执行内连接
# 仅提取people_num为1且is_business为True的数据
pd.merge(reserve_tb, hotel_tb, on='hotel_id', how='inner') \
  .query('people_num == 1 & is_business')

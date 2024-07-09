from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd

customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
res = pd.merge(reserve_tb.query('people_num == 1'),
               hotel_tb.query('is_business'),
               on='hotel_id', how='inner')
print(res)

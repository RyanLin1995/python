import numpy as np
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
reserve_tb['total_price_log'] = \
  reserve_tb['total_price'].apply(lambda x: np.log(x / 1000 + 1))

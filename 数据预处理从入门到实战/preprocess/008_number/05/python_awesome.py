import numpy as np
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
reserve_tb = reserve_tb[
  (abs(reserve_tb['total_price'] - np.mean(reserve_tb['total_price'])) /
   np.std(reserve_tb['total_price']) <= 3)
].reset_index()

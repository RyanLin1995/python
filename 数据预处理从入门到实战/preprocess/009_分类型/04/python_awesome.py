import pandas as pd
import numpy as np
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
customer_tb['sex_and_age'] = pd.Categorical(
  # 提取要拼接的列
  customer_tb[['sex', 'age']]

    # 在lambda函数内将sex和以10岁为间隔的age也字符串的形式进行拼接，中间用“_”相连 
    .apply(lambda x: '{}_{}'.format(x[0], np.floor(x[1] / 10) * 10),
           axis=1)
)

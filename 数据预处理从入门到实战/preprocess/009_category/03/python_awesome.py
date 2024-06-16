import pandas as pd
import numpy as np
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 通过pd.Categorical函数将转换为category类型
customer_tb['age_rank'] = \
  pd.Categorical(np.floor(customer_tb['age']/10)*10)

# 在主数据中添加“60岁以上”
customer_tb['age_rank'].cat.add_categories(['60岁以上'], inplace=True)

# 更改要聚合的数据
# 由于category 类型仅能进行“==”或“!=”的判断，所以这里使用isin函数
customer_tb.loc[customer_tb['age_rank'] \
           .isin([60.0, 70.0, 80.0]), 'age_rank'] = '60岁以上'

# 删除未使用的主数据                
customer_tb['age_rank'].cat.remove_unused_categories(inplace=True)

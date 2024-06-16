import pandas as pd
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 在哑变量化之前先转换为分类型
customer_tb['sex'] = pd.Categorical(customer_tb['sex'])

# 通过get_dummies函数实现sex的哑变量化
# 当drop_first为False时，生成分类值的所有种类的值的哑变量标志
dummy_vars = pd.get_dummies(customer_tb['sex'], drop_first=False)

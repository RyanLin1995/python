from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 添加布尔类型列，sex值为man时该列元素为TRUE
# 以下代码不使用astype函数也可实现布尔类型转换
customer_tb[['sex_is_man']] = (customer_tb[['sex']] == 'man').astype('bool')

# 将sex转换为分类型
customer_tb['sex_c'] = \
  pd.Categorical(customer_tb['sex'], categories=['man', 'woman'])

# 
# astype也可实现分类型的转换
# customer_tb['sex_c'] = customer_tb['sex_c'].astype('category')

# 索引数据存储在codes中 
customer_tb['sex_c'].cat.codes

# 主数据存储在categories中
customer_tb['sex_c'].cat.categories

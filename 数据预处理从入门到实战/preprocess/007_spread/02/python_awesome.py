import pandas as pd
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 导入稀疏矩阵的库 
from scipy.sparse import csc_matrix

# 生成不同顾客ID和不同住宿人数的预订次数的表
cnt_tb = reserve_tb \
  .groupby(['customer_id', 'people_num'])['reserve_id'].size() \
  .reset_index()
cnt_tb.columns = ['customer_id', 'people_num', 'rsv_cnt']

# 将稀疏矩阵的行和列所对应的值转换为分类型
# 关于分类型数据，详见第9 章 
customer_id = pd.Categorical(cnt_tb['customer_id'])
people_num = pd.Categorical(cnt_tb['people_num'])

# 生成稀疏矩阵
# 第1个参数是将指定的矩阵所对应的值、行号数组和列号数组汇总而成的元组
# 将shape 参数指定为稀疏矩阵的维度（设置为行数和列数的元组）
# （customer_id.codes用于获取索引号）
# （len(customer_id.categories)用于对customer_id 进行唯一值计数）
csc_matrix((cnt_tb['rsv_cnt'], (customer_id.codes, people_num.codes)),
           shape=(len(customer_id.categories), len(people_num.categories)))

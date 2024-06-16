from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# reserve_tb['customer_id'].unique()将返回去重复后的customer_id
# 为利用sample函数，先把去重后的列值转换成pandas.Series（pandas的list对象）
# 通过sample函数对顾客ID进行采样
target = pd.Series(reserve_tb['customer_id'].unique()).sample(frac=0.5)

# 通过isin函数提取customer_id值与采样得到的顾客ID的值一致的数据行
reserve_tb[reserve_tb['customer_id'].isin(target)]

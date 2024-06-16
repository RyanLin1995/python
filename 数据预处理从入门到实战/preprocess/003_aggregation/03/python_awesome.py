from preprocess.load_data.data_loader import load_hotel_reserve
import numpy as np

customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 将max、min、mean和median函数应用于total_price
# 使用Python中的lambda表达式指定agg函数中的聚合操作
# 在lambda表达式中指定numpy.percentile，计算百分位数（百分数指定为20）
result = reserve_tb \
    .groupby('hotel_id') \
    .agg({'total_price': ['max', 'min', 'mean', 'median',
                          lambda x: np.percentile(x, q=20)]}) \
    .reset_index()
result.columns = ['hotel_id', 'price_max', 'price_min', 'price_mean',
                  'price_median', 'price_20per']
print(result)

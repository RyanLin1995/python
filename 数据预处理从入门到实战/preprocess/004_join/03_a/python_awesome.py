from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 对每个顾客按reserve_datetime进行排序
# 在使用group_by函数后通过apply函数对每个分组排序
# 通过sort_values函数对数据排序，axis为0表示按行排序，axis为1表示按列排序
result = reserve_tb \
  .groupby('customer_id') \
  .apply(lambda group:
         group.sort_values(by='reserve_datetime', axis=0, inplace=False))

# result已经按customer_id分组
# 对每个顾客取其total_price列中往　前数第2条记录的值，并将其保存为before_price
# shift函数用于将数据行向下偏移，偏移行数即periods参数的值
result['before_price'] = \
  result['total_price'].groupby('customer_id').shift(periods=2)

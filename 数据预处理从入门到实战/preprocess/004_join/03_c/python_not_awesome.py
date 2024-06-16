from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 对每个customer_id按reserve_datetime列对数据排序
result = reserve_tb.groupby('customer_id') \
  .apply(lambda x: x.sort_values(by='reserve_datetime', ascending=True)) \
  .reset_index(drop=True)

# 添加新列price_avg
result['price_avg'] = pd.Series(
  result
    # 对每个customer_id，把total_price的窗口切分为3个并汇总，然后计算其平均值
    # 把min_periods设置为1，表示当记录数为1以上时进行计算
    .groupby('customer_id')
    ['total_price'].rolling(center=False, window=3, min_periods=1).mean()

    # 取消分组，同时删除customer_id列
    .reset_index(drop=True)
)

# 对每个customer_id，将price_avg下移1行
result['price_avg'] = \
  result.groupby('customer_id')['price_avg'].shift(periods=1)
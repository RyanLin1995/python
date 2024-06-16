from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 对每个customer_id按reserve_datetime进行排序
result = reserve_tb.groupby('customer_id') \
  .apply(lambda x: x.sort_values(by='reserve_datetime', ascending=True)) \
  .reset_index(drop=True)

# 添加新列price_sum
result['price_sum'] = pd.Series(
    # 仅提取所需的数据列
    result.loc[:, ["customer_id", "total_price"]]

    # 对每个customer_id，把total_price的窗口切分为3个并汇总，然后计算合计值
    .groupby('customer_id')
    .rolling(center=False, window=3, min_periods=3).sum()

    # 取消分组，同时取出total_price列
    .reset_index(drop=True)
    .loc[:, 'total_price']
)
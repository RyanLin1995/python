from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
import pandas.tseries.offsets as offsets
import operator

# 为了进行日期计算，这里将数据类型由字符串转换为日期型（详见第10章）
reserve_tb['reserve_datetime'] = \
  pd.to_datetime(reserve_tb['reserve_datetime'], format='%Y-%m-%d %H:%M:%S')

# 在不确认reserve_datetime中的日期的情况下，将customer_id相同的数据行全部连接 
sum_table = pd.merge(
	reserve_tb[['reserve_id', 'customer_id', 'reserve_datetime']],
  reserve_tb[['customer_id', 'reserve_datetime', 'total_price']]
            .rename(columns={'reserve_datetime': 'reserve_datetime_before'}),
  on='customer_id')

# 比较checkin列的日期，仅提取连接了90天内的数据的数据行
# 使用operator中的and_函数，设置复合条件
# 按reserve_id计算total_price的合计值
# （关于日期时间型，详见第10章）
sum_table = sum_table[operator.and_(
  sum_table['reserve_datetime'] > sum_table['reserve_datetime_before'],
  sum_table['reserve_datetime'] + offsets.Day(-90) <= sum_table['reserve_datetime_before']
)].groupby('reserve_id')['total_price'].sum().reset_index()

# 设置列名
sum_table.columns = ['reserve_id', 'total_price_sum']

# 连接计算出的合计值，将合计值信息加入源表中
# 使用fillna将不存在合计值的记录的值设置为0
pd.merge(reserve_tb, sum_table, on='reserve_id', how='left').fillna(0)

from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 用于处理日期型的库
import datetime
# 用于计算日期的库
from dateutil.relativedelta import relativedelta

# 生成年月主表
month_mst = pd.DataFrame({
  'year_month':
    # 用relativedelta实现从2017-01-01向后推x个月，x取值为0、1、2
    # 生成2017-01-01, 2017-02-01和2017-03-01的列表
    [(datetime.date(2017, 1, 1) + relativedelta(months=x)).strftime("%Y%m")
     for x in range(0, 3)]
})

# 为了进行交叉连接，准备全部为相同值的连接键
customer_tb['join_key'] = 0
month_mst['join_key'] = 0

# 用准备的连接键对customer_tb和month_mst执行内连接，从而实现交叉连接
customer_mst = pd.merge(
  customer_tb[['customer_id', 'join_key']], month_mst, on='join_key'
)

#  在预定记录表中准备年月的连接键 
reserve_tb['year_month'] = reserve_tb['checkin_date'] \
  .apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d').strftime("%Y%m"))

#  与预订记录连接，计算住宿费总额
summary_result = pd.merge(
  customer_mst,
  reserve_tb[['customer_id', 'year_month', 'total_price']],
  on=['customer_id', 'year_month'], how='left'
).groupby(['customer_id', 'year_month'])["total_price"] \
 .sum().reset_index()

# 将不存在预订记录时的住宿费总额由空值转换为0
summary_result.fillna(0, inplace=True)

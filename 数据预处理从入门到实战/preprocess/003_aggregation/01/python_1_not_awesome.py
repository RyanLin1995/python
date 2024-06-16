from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 使用groupby函数将reserve_id指定为聚合单元，使用size函数计算数据条数
# 由于groupby 函数的聚合处理，行号变得不连续
# 通过reset_index函数将指定为聚合单元的hotel_id从聚合状态还原为列名
# 将新行名修改为当前行号
rsv_cnt_tb = reserve_tb.groupby('hotel_id').size().reset_index()

# 设置聚合结果的列名
rsv_cnt_tb.columns = ['hotel_id', 'rsv_cnt']

# 使用groupby将hotel_id指定为聚合单元
# 通过customer_id的值调用nunique函数，计算顾客数
cus_cnt_tb = \
  reserve_tb.groupby('hotel_id')['customer_id'].nunique().reset_index()

# 设置聚合结果的列名
cus_cnt_tb.columns = ['hotel_id', 'cus_cnt']

# 使用merge函数，以hotel_id作为连接键执行连接处理（详见第4章）
pd.merge(rsv_cnt_tb, cus_cnt_tb, on='hotel_id')

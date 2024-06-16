from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 使用agg函数统一指定聚合处理
# 对reserve_id应用count函数
# 对customer_id应用nunique函数
result = reserve_tb \
  .groupby('hotel_id') \
  .agg({'reserve_id': 'count', 'customer_id': 'nunique'})

# 通过reset_index函数重新分配列号（由于inplace=True，程序将直接更新result）
result.reset_index(inplace=True)
result.columns = ['hotel_id', 'rsv_cnt', 'cus_cnt']

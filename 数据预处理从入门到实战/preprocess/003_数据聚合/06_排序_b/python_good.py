from preprocess.load_data.data_loader import load_hotel_reserve

customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 计算预订次数（详见3-1节）
rsv_cnt_tb = reserve_tb.groupby('hotel_id').size().reset_index()
rsv_cnt_tb.columns = ['hotel_id', 'rsv_cnt']

# 基于预订次数计算位次
# 通过将ascendin设置为False，指定为降序排列
# 将method指定为min，表示值相同时可以采用的最小位次 
rsv_cnt_tb['rsv_cnt_rank'] = rsv_cnt_tb['rsv_cnt'].rank(ascending=False, method='min')

# 剔除不需要的rsv_cnt列
rsv_cnt_tb.drop('rsv_cnt', axis=1, inplace=True)

print(rsv_cnt_tb)

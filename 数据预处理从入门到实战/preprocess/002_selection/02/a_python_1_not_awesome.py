from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 通过为数组指定条件表达式，提取满足条件的行
# 通过DataFrame的特定列的不等式，返回以判段结果True或False为元素的数组
# 将条件表达式用“&”连接，返回元素为True或False的数组，仅当判断结果同时为True时，其元素才为True
reserve_tb[(reserve_tb['checkout_date'] >= '2016-10-13') &
           (reserve_tb['checkout_date'] <= '2016-10-14')]

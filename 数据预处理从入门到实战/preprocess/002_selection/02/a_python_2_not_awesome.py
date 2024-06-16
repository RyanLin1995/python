from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 为loc函数二维数组的第一维度指定条件，提取满足条件的行
# 为loc函数二维数组的第二维度指定“:”，提取所有列
reserve_tb.loc[(reserve_tb['checkout_date'] >= '2016-10-13') &
               (reserve_tb['checkout_date'] <= '2016-10-14'), :]

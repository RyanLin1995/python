from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 将iloc函数二维数组的第一维度指定为“:”，提取所有行
# 将iloc函数二维数组的第二维度指定为由列号组成的数组，提取相应的列
# 0:6和[0, 1, 2, 3, 4, 5]表示相同的意思
reserve_tb.iloc[:, 0:6]

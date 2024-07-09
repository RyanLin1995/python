from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 用drop函数删除不需要的列
# axis=1表示按列删除
# inplace=True表示使更改作用于reserve_tb
reserve_tb.drop(['people_num', 'total_price'], axis=1, inplace=True)

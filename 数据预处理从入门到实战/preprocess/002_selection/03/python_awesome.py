from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 从reserve_tb中采样50%
reserve_tb.sample(frac=0.5)


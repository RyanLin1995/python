from preprocess.load_data.data_loader import load_hotel_reserve

customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 通过round函数进行四舍五入后，用mode函数计算众数 
print(reserve_tb['total_price'].round(-3).mode())

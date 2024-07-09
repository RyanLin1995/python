from preprocess.load_data.data_loader import load_hotel_reserve

customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 对total_price列应用var和std函数，计算方差和标准差
result = reserve_tb \
    .groupby('hotel_id') \
    .agg({'total_price': ['var', 'std']}).reset_index()
result.columns = ['hotel_id', 'price_var', 'price_std']

# 由于当数据条数为1时方差和标准差会变为na，所以这里将其替换为0
result.fillna(0, inplace=True)
print(result)

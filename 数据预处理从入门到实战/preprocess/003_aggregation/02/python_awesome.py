from preprocess.load_data.data_loader import load_hotel_reserve

customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 将聚合单元指定为hotel_id和people_num的组合
# 从聚合后的数据中取出total_price，调用sum函数计算住宿费总额
result = reserve_tb.groupby(['hotel_id', 'people_num'])['total_price'].sum().reset_index()

# 将住宿费总额的列名为total_price，所以这里将其更改为price_sum
result.rename(columns={'total_price': 'price_sum'}, inplace=True)

print(result)

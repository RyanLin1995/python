from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 在reserve_tb 中指定包含列名的字符串数组，提取相应的列
reserve_tb[['reserve_id', 'hotel_id', 'customer_id',
            'reserve_datetime', 'checkin_date', 'checkin_time',
            'checkout_date']]

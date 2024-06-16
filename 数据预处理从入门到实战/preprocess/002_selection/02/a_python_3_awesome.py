from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
reserve_tb.query('"2016-10-13" <= checkout_date <= "2016-10-14"')

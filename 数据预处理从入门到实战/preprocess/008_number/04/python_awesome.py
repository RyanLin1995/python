from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
from sklearn.preprocessing import StandardScaler

# 为了对小数点后面的部分进行处理，将数据转换为float类型
reserve_tb['people_num'] = reserve_tb['people_num'].astype(float)

# 生成用于进行归一化的对象
ss = StandardScaler()

# fit_transform函数可同时实现fit函数（归一化前的准备性计算）
# 和transform（根据准备好的信息进行归一化的转换处理）的功能
result = ss.fit_transform(reserve_tb[['people_num', 'total_price']])

reserve_tb['people_num_normalized'] = [x[0] for x in result]
reserve_tb['total_price_normalized'] = [x[1] for x in result]

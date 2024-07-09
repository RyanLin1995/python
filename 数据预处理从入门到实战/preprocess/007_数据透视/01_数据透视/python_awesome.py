import pandas as pd
from preprocess.load_data.data_loader import load_hotel_reserve

customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 用pivot_table同时实现横向显示和聚合处理
# 向aggfunc参数指定用于计算预订次数的函数

# pivot_table 函数的第 1 个参数指定的是对象表，index 参数指定的是表示数据集合的键值，
# columns 参数指定的是表示数据元素类别的键值，而 values 参数指定的是数据元素值对应的对象列（可通过数组形式指定多个index和columns 参数）。
# 此外，aggfunc 参数指定的是用于将 values 参数指定的列值转换为数据元素值的函数。在 fill_value 参数中设置值，可以指定当相应列值不存在时数据元素的填充值。
df = pd.pivot_table(reserve_tb, index='customer_id', columns='people_num',
                    values='reserve_id', aggfunc=lambda x: len(x), fill_value=0)

print(df)

from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd

customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 为使用rank函数进行排序，将数据类型由字符串转换为timestamp类型（详见第10章）
reserve_tb['reserve_datetime'] = pd.to_datetime(
    reserve_tb['reserve_datetime'], format='%Y-%m-%d %H:%M:%S'
)

# 添加新列log_no
# 使用group_by指定聚合单元
# 按顾客统一生成reserve_datetime，然后使用rank函数生成位次
# 把ascending设置为True，即按升序排列（False表示降序排列）
reserve_tb['log_no'] = reserve_tb \
    .groupby('customer_id')['reserve_datetime'] \
    .rank(ascending=True, method='first')

print(reserve_tb)

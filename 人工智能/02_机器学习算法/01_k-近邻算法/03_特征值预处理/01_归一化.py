import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('dating.txt')

# 归一化：通过对原始数据进行变换把数据映射到(默认为[0,1])之间，注意最大值最小值是变化的，
# 另外，最大值与最小值非常容易受异常点影响，所以这种方法鲁棒性较差，只适合传统精确小数据场景。

# 1 实例化一个转换器
transfer = MinMaxScaler(feature_range=(0, 1))  # feature_range 参数指定范围，默认(0,1)
# 2 调用 fit_transform 方法
minmax_data = transfer.fit_transform(
    data[['milage', 'Liters', 'Consumtime']])  # 需传入 numpy array 格式的数据，返回值是转换后的形状相同的array
print(minmax_data)

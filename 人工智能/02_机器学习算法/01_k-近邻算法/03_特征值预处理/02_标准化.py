import pandas
from sklearn.preprocessing import StandardScaler

data = pandas.read_csv('dating.txt')

# 标准化：通过对原始数据进行变换把数据变换到均值为 0,标准差为 1 范围内。在已有样本足够多的情况下比较稳定，适合现代嘈杂大数据场景。
# 1. 实例化一个转换器
transfer = StandardScaler()  # 处理之后所有数据都聚集在均值0附近，标准差为1
# 2. 调用 fit_transform 方法
standard_data = transfer.fit_transform(data[['milage', 'Liters', 'Consumtime']])
print(standard_data)

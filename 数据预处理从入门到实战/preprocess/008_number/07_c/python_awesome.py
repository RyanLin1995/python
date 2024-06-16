import numpy as np
from preprocess.load_data.data_loader import load_production_missing_num
production_miss_num = load_production_missing_num()

# 本书刊登内容如下
# 通过replace函数将None转换为nan
production_miss_num.replace('None', np.nan, inplace=True)

# 将thickness转换为数值型(由于None字符串混在其中，所以不是数值型)
production_miss_num['thickness'] = \
  production_miss_num['thickness'].astype('float64')

# 计算thickness的平均值
thickness_mean = production_miss_num['thickness'].mean()

# 用thickness的平均值填充thickness的缺失值
production_miss_num['thickness'].fillna(thickness_mean, inplace=True)


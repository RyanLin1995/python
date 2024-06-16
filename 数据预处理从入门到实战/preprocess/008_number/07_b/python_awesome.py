import numpy as np
from preprocess.load_data.data_loader import load_production_missing_num
production_miss_num = load_production_missing_num()

# 本书刊登内容如下
# 通过replace函数将None转换为nan
production_miss_num.replace('None', np.nan, inplace=True)

# 通过fillna函数将thickness的缺失值填充为1
production_miss_num['thickness'].fillna(1, inplace=True)

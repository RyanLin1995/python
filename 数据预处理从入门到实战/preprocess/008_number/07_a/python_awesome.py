import numpy as np
from preprocess.load_data.data_loader import load_production_missing_num
production_miss_num = load_production_missing_num()

# 本书刊登内容如下
# 通过replace函数将None转换为nan
# (指定None时必须以字符串的形式指定)
production_miss_num.replace('None', np.nan, inplace=True)

# 通过drop_na函数删除thickness为nan的记录
production_miss_num.dropna(subset=['thickness'], inplace=True)

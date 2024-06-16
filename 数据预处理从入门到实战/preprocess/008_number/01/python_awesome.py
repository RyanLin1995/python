import pandas as pd

# 本书刊登内容如下
# 确认数据类型
type(40000 / 3)

# 转换为整数型
int(40000 / 3)

# 转换为浮点型
float(40000 / 3)

df = pd.DataFrame({'value': [40000 / 3]})

# 确认数据类型
df.dtypes

# 转换为整数型
df['value'].astype('int8')
df['value'].astype('int16')
df['value'].astype('int32')
df['value'].astype('int64')

# 转换为浮点型
df['value'].astype('float16')
df['value'].astype('float32')
df['value'].astype('float64')
df['value'].astype('float128')

# 可以按如下方式指定Python的数据类型
df['value'].astype(int)
df['value'].astype(float)

import numpy as np
from preprocess.load_data.data_loader import load_production_missing_category
production_missc_tb = load_production_missing_category()

# 本书内容刊登如下
# 从sklearn库中导入KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier

# 通过replace函数将None转换为nan
production_missc_tb.replace('None', np.nan, inplace=True)

# 提取无缺失值的数据 
train = production_missc_tb.dropna(subset=['type'], inplace=False)

# 提取包含缺失值的数据
test = production_missc_tb \
  .loc[production_missc_tb.index.difference(train.index), :]

# 生成knn模型，n_neighbors是knn的k参数
kn = KNeighborsClassifier(n_neighbors=3)

# 训练knn模型
kn.fit(train[['length', 'thickness']], train['type'])

# 用knn模型计算预测值并填充type
test['type'] = kn.predict(test[['length', 'thickness']])

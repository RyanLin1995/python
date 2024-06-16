from preprocess.load_data.data_loader import load_production
production_tb = load_production()

# 本书刊登内容如下
# 导入PCA
from sklearn.decomposition import PCA

# 将n_components 设置为用主成分分析进行变换后的维数
pca = PCA(n_components=2)

# 实现主成分分析
# 主成分分析的变换参数保存在pca 中，主成分分析后的值以返回值形式返回
pca_values = pca.fit_transform(production_tb[['length', 'thickness']])

# 确认累计贡献率和贡献率
print('累计贡献率: {0}'.format(sum(pca.explained_variance_ratio_)))
print('各维度的贡献率: {0}'.format(pca.explained_variance_ratio_))

# 使用predict函数实现同样的降维处理
pca_newvalues = pca.transform(production_tb[['length', 'thickness']])

# 什么是主成分分析(PCA)
# 定义：高维数据转化为低维数据的过程，在此过程中可能会舍弃原有数据、创造新的变量
# 作用：是数据维数压缩，尽可能降低原数据的维数（复杂度），损失少量信息。
# 应用：回归分析或者聚类分析当中
from sklearn.decomposition import PCA
from sklearnex import patch_sklearn

patch_sklearn()
data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]
# 保留到多少维度
transfer = PCA(n_components=2)  # n_components 如果传入小数：表示保留百分之多少的信息，如果传入整数：减少到多少特征
trans_data = transfer.fit_transform(data)
print(trans_data)

# 保留信息百分比
transfer = PCA(n_components=0.9)  # n_components 如果传入小数：表示保留百分之多少的信息，如果传入整数：减少到多少特征
trans_data = transfer.fit_transform(data)
print(trans_data)

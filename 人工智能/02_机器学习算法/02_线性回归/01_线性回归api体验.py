from sklearn.linear_model import LinearRegression
from sklearnex import patch_sklearn

patch_sklearn()

# 获取数据
x = [[80, 86],
     [82, 80],
     [85, 78],
     [90, 90],
     [86, 82],
     [82, 90],
     [78, 80],
     [92, 94]]  # 平时跟期末成绩
y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]  # 得到的成绩

# 模型训练
# 1. 实例化一个估计器
estimator = LinearRegression()

# 2. 调用 fit 方法进行模型训练
estimator.fit(x, y)

# 查看系数值
coef = estimator.coef_  # 获取回归系数值
print('系数是:', coef)

# 预测
print('预测值是:', estimator.predict([[80, 100]]))

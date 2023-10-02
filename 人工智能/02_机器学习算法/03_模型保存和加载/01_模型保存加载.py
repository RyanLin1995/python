import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
import joblib

from sklearnex import patch_sklearn

patch_sklearn()

# 1.获取数据
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# 2.数据集划分
x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=22, test_size=0.3)

# 3.特征工程——标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)

# 4.机器学习——线性回归（岭回归）
# # 4.1 模型训练
# estimator = Ridge()
# estimator.fit(x_train, y_train)
#
# # 4.2 模型保存
# joblib.dump(estimator, 'test.pkl')

# 4.3 模型加载
estimator = joblib.load('test.pkl')

# 5.模型评估
# 5.1 预测值和准确率
y_predict = estimator.predict(x_test)
print("预测值为:\n", y_predict)

score = estimator.score(x_test, y_test)
print("准确率为:\n", score)

# 5.2 均方误差
error = mean_squared_error(y_test, y_predict)
print("误差为:\n", error)

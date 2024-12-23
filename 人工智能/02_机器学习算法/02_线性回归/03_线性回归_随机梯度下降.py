import numpy as np
import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearnex import patch_sklearn

patch_sklearn()

# 1.获取数据
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]


def liner_sgd():
    """
        线性回归——随机梯度下降
    """
    # 2.数据集划分
    x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=22, test_size=0.3)

    # 3.特征工程
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 4.机器学习——线性回归（随机梯度下降）
    estimator = SGDRegressor(max_iter=1000)  # 随机梯度下降 API，支持不同的 loss 函数和正则化惩罚项来拟合线性回归模型。
    # loss: 损失类型，默认是squared_error（普通最小二乘法）
    # fit_intercept：是否计算偏置
    # learning_rate: 学习率填充
    # * --> 'constant': eta = eta0
    # * --> 'optimal': eta = 1.0 / (alpha * (t + t0))
    # * --> 'invscaling'[default]: eta = eta0 / pow(t, power_t)，其中 power_t = 0.25，存在父类当中
    # 对于一个常数值的学习率来说，可以使用learning_rate =‘constant’，并使用eta0来指定学习率。
    estimator.fit(x_train, y_train)

    # 5.模型评估
    # 5.1 获取系数值
    y_predict = estimator.predict(x_test)
    print("预测值为:\n", y_predict)
    print("模型中的系数为:\n", estimator.coef_)
    print("模型中的偏置为:\n", estimator.intercept_)
    # 5.2 获取准确率
    score = estimator.score(x_test, y_test)
    print("准确率为:\n", score)
    # 5.3 评估
    error = mean_squared_error(y_test, y_predict)
    print("误差为:\n", error)


if __name__ == '__main__':
    liner_sgd()

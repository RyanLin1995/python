import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
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


def liner_formal_equation():
    """
        线性回归——正规方程 API 使用
    """
    # 2.数据集划分
    x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=22, test_size=0.3)

    # 3.特征工程——标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 4.机器学习——线性回归（正规方程）
    estimator = LinearRegression(n_jobs=-1)  # 正规方程 API。fit_intercept 是否计算偏置。其参数coef_：回归系数；intercept_：偏置
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
    error = mean_squared_error(y_test,
                               y_predict)  # 均方误差(Mean Squared Error)MSE)评价机制（均方差回归损失）。y_true:真实值，y_pred:预测值。返回的是浮点数结果
    print("误差为:\n", error)


if __name__ == '__main__':
    liner_formal_equation()

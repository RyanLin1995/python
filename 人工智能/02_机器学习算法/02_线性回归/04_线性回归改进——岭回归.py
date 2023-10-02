# Ridge 岭回归——具有l2正则化的线性回归

# L2正则化
# 作用：可以使得其中一些W的都很小，都接近于0，削弱某个特征的影响
# 优点：越小的参数说明模型越简单，越简单的模型则越不容易产生过拟合现象

# 参数：
# alpha: 正则化力度，也叫 λ，λ 取值：0~1 1~10
# solver: 会根据数据自动选择优化方法，推荐用sag。 sag: 如果数据集、特征都比较大，选择该随机梯度下降优化
# normalize: 数据是否进行标准化。如果 normalize=False，可以在 fit 之前调用 preprocessing.StandardScaler 标准化数据
# Ridge.coef_:回归权重
# Ridge.intercept_:回归偏置

# Ridge方法相当于 SGDRegressor(penalty='l2', loss="squared_loss")，只不过SGDRegressor实现了一个普通的随机梯度下降学习，推荐使用Ridge(实现了SAG)

# RidgeCV(_BaseRidgeCV, RegressorMixin)——具有 l2 正则化的线性回归，可以进行交叉验证

# 注意：
# 正则化力度越大，权重系数会越小
# 正则化力度越小，权重系数会越大

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge, RidgeCV
from sklearnex import patch_sklearn

patch_sklearn()

# 1.获取数据
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]


def linear_ridge():
    """
        线性回归——岭回归
    """
    # 2. 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(data, target, random_state=22, test_size=0.3)

    # 3. 数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 4. 机器学习（线性回归——岭回归）
    estimator = Ridge()
    # estimator = RidgeCV(alphas=(0.1, 1, 10))
    estimator.fit(x_train, y_train)

    # 5. 模型评估
    # 5.1 获取评估值
    y_predict = estimator.predict(x_test)
    print("预测值为:\n", y_predict)
    print("模型中的系数为:\n", estimator.coef_)
    print("模型中的偏置为:\n", estimator.intercept_)
    # 5.2 获取准确值
    score = estimator.score(x_test, y_test)
    print("准确率为:\n", score)
    # 5.3 评估
    error = mean_squared_error(y_test, y_predict)
    print("误差为:\n", error)


if __name__ == '__main__':
    linear_ridge()

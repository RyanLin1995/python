import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearnex import patch_sklearn

patch_sklearn()


def vat_thr():
    """
    特征选择：低方差特征过滤，即把方差小的列剔除
    """
    data = pd.read_csv('data\\factor_returns.csv')
    print(data)

    transfer = VarianceThreshold(threshold=10)  # 如果不添加 threshold 是只会剔除完全相等的值。
    transfer_data = transfer.fit_transform(data.iloc[:, 1:10])  # 获取第二到第十列的数据

    print("之前数据形状：\n", data.iloc[:, 1:10].shape)
    print("之后数据形状：\n", transfer_data.shape)


if __name__ == '__main__':
    vat_thr()

from sklearn.feature_extraction import DictVectorizer  # 字典特征提取 api
from sklearnex import patch_sklearn

patch_sklearn()


def dict_demo():
    """
    字典特征提取
    """
    data = [{'city': '北京', 'temperature': 100},
            {'city': '上海', 'temperature': 60},
            {'city': '深圳', 'temperature': 30}]
    # 字典特征提取
    # 1. 实例化
    transfer = DictVectorizer(sparse=True)  # sparse 矩阵为 TRUE 时输出信息详解如下：
    # sparse 矩阵可以节省内存和提高读取效率
    """
    (0, 1) 1.0  表示第0行第1列的值为 1.0
    (0, 3) 100.0  表示第0行第3列的值为 100.0
    (1, 0) 1.0
    (1, 3) 60.0
    (2, 2) 1.0
    (2, 3) 30.0
    """

    # 2. 调用 fit_transform
    trans_data = transfer.fit_transform(data)

    # 打印特征名字
    print("特征名字：\n", transfer.get_feature_names_out())
    print(trans_data)


if __name__ == '__main__':
    dict_demo()

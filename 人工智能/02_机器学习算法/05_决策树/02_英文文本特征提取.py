from sklearn.feature_extraction.text import CountVectorizer
from sklearnex import patch_sklearn

patch_sklearn()


def count_text_demo():
    """
    英文文本特征提取，并返回词频矩阵
    """
    data = ["life is short,i like like python",
            "life is too long,i dislike python"]
    # 1. 实例化
    transfer = CountVectorizer()  # 没有 sparse 矩阵参数，且单个字母和标点符号不做统计

    # 2. 调用 fit_transform
    transfer_data = transfer.fit_transform(data)

    print(transfer.get_feature_names_out())
    print(transfer_data.toarray())  # 结果为一个矩阵数组
    # [[0 1 1 2 0 1 1 0] [1 1 1 0 1 1 0 1]] 第一个数组为第一句话，第二个数组为第二句话，次数为 transfer.get_feature_names_out() 输出结果对应在每一句话出现的次数


if __name__ == '__main__':
    count_text_demo()

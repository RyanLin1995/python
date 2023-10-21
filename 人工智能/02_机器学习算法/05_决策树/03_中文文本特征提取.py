from sklearn.feature_extraction.text import CountVectorizer
from sklearnex import patch_sklearn
import pkuseg

patch_sklearn()


def count_text_demo():
    """
    中文文本特征提取，并返回词频矩阵
    """
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

    data_list = []
    for i in data:
        data_list.append(cut_word(i))
    print(data_list)

    # 1. 实例化
    transfer = CountVectorizer(stop_words=["一种", "还是"])  # stop_words：所有这些停用词都将从结果标记中删除

    # 2. 调用 fit_transform
    transfer_data = transfer.fit_transform(data_list)

    print(transfer.get_feature_names_out())
    print(transfer_data.toarray())


def cut_word(sen):
    """
    中文分词
    """
    seg = pkuseg.pkuseg()
    return ' '.join(seg.cut(sen))


if __name__ == '__main__':
    count_text_demo()

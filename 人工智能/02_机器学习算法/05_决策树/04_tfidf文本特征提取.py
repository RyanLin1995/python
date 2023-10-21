from sklearn.feature_extraction.text import TfidfVectorizer
from sklearnex import patch_sklearn
import pkuseg


def cut_word(text):
    seg = pkuseg.pkuseg()
    return ' '.join(seg.cut(text))


def chinese_text_tfidf_demo():
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    text_list = []
    for i in data:
        text_list.append(cut_word(i))

    # 1. 实例化一个转换器
    transfer = TfidfVectorizer(stop_words=['一种', '不会', '不要'])

    # 2. 调用 fit_transform
    data = transfer.fit_transform(text_list)
    print("文本特征抽取的结果：\n", data.toarray())
    print("返回特征名字：\n", transfer.get_feature_names_out())


if __name__ == '__main__':
    chinese_text_tfidf_demo()

"""
文本序列化
"""

from collections import Counter

import numpy as np

from utils import tokenize


class WordSequence:
    UNK_TAG = "<UNK>"  # 表示未知字符
    PAD_TAG = "<PAD>"  # 填充符
    PAD = 0
    UNK = 1

    def __init__(self):
        self.inverse_dict = None
        self.dict = {  # 保存词语和对应的数字
            self.UNK_TAG: self.UNK,
            self.PAD_TAG: self.PAD,
        }
        self.count = {}  # 统计词频的
        self.is_fit = False

    def to_index(self, word):
        """word -> index"""
        assert self.is_fit == True, "必须先进行fit操作"
        return self.dict.get(word, self.UNK)

    def to_word(self, index):
        """index -> word"""
        assert self.is_fit, "必须先进行fit操作"
        if index in self.inverse_dict:
            return self.inverse_dict[index]
        return self.UNK_TAG

    def fit(self, sentence):
        """
        接受句子，统计词频
        :param sentence:[str,str,str]
        :return:None
        """
        for word in sentence:
            self.count[word] = (
                self.count.get(word, 0) + 1
            )  # 所有的句子fit之后，self.count就有了所有词语的词频
        self.is_fit = True

    def build_vocab(self, min_count=0, max_count=None, max_features=None):
        """
        fit 方法的主要作用是根据输入的句子集合构建一个词典（self.dict），并将每个单词映射到唯一的索引值。同时，它还生成一个反向字典（self.inversed_dict），用于后续从索引值还原为单词。
        :param min_count: 最小出现的次数
        :param max_count: 最大出现的次数
        :param max_features: 总词语的最大数量
        :return:
        """

        # 比最小的数量大和比最大的数量小的需要
        if min_count is not None:
            self.count = {k: v for k, v in self.count.items() if v >= min_count}
        if max_count is not None:
            self.count = {k: v for k, v in self.count.items() if v <= max_count}

        # 限制最大的数量
        if isinstance(max_features, int):
            count = sorted(list(self.count.items()), key=lambda x: x[1])
            if len(count) > max_features:
                count = count[-int(max_features) :]
            for w, _ in count:
                self.dict[w] = len(self.dict)
        else:
            for w in sorted(self.count):
                self.dict[w] = len(self.dict)

        # 把dict进行翻转
        self.inverse_dict = dict(zip(self.dict.values(), self.dict.keys()))

    def transform(self, sentence, max_len=None):
        """
        transform 方法的主要作用是将输入的句子转换为数值序列（向量）。它利用 fit 方法生成的词典，将每个单词替换为其对应的索引值。
        :param sentence:
        :param max_len:
        :return:
        """
        assert self.is_fit, "必须先进行fit操作"
        if max_len is not None:
            r = [self.PAD] * max_len
        else:
            r = [self.PAD] * len(sentence)
        if max_len is not None and len(sentence) > max_len:
            sentence = sentence[:max_len]
        for index, word in enumerate(sentence):
            r[index] = self.to_index(word)
        return np.array(r, dtype=np.int64).tolist()

    def inverse_transform(self, insides):
        """
        把数字序列转化为字符
        :param insides: [int,int,int]
        :return: [str,str,str]
        """
        return [self.inverse_dict.get(i, "<UNK>") for i in insides]

    def __len__(self):
        return len(self.dict)


if __name__ == "__main__":
    # sentences = [["今天", "天气", "很", "好"], ["今天", "去", "吃", "什么"]]
    # ws = WordSequence()
    # for sentence in sentences:
    #     ws.fit(sentence)
    # ws.build_vocab(min_count=1)
    # print(ws.dict)
    # ret = ws.transform(
    #     ["好", "好", "好", "好", "好", "好", "好", "热", "呀"], max_len=3
    # )
    # print(ret)
    # ret = ws.inverse_transform(ret)
    # print(ret)
    import pickle
    import os
    from tqdm import tqdm

    ws = WordSequence()
    train_data_path = "data\\aclImdb\\train"
    temp_data_path = [train_data_path + "\\pos", train_data_path + "\\neg"]
    total_file_path = []  # 所有评论的文件路劲
    for i in temp_data_path:
        file_name_list = os.listdir(i)
        file_path_list = [os.path.join(i, j) for j in file_name_list]
        total_file_path.extend(file_path_list)

    for file in tqdm(total_file_path):
        with open(file, "r", encoding="utf-8") as f:
            un_fit_sentence = tokenize(f.read())
            ws.fit(un_fit_sentence)

    ws.build_vocab(min_count=10)
    print(len(ws))
    pickle.dump(ws, open("./models/ws.pkl", "wb"))
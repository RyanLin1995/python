import numpy as np
from collections import Counter


class Word2Sequence:
    UNK_TAG = "UNK"
    PAD_TAG = "PAD"

    UNK = 0
    PAD = 1

    def __init__(self):
        self.inversed_dict = None
        self.dict = {self.UNK_TAG: self.UNK, self.PAD_TAG: self.PAD}
        self.fited = False

    def to_index(self, word):
        """word -> index"""
        assert self.fited == True, "必须先进行fit操作"
        return self.dict.get(word, self.UNK)

    def to_word(self, index):
        """index -> word"""
        assert self.fited, "必须先进行fit操作"
        if index in self.inversed_dict:
            return self.inversed_dict[index]
        return self.UNK_TAG

    def __len__(self):
        return self

    def fit(self, sentences, min_count=1, max_count=None, max_feature=None):
        """
        fit 方法的主要作用是根据输入的句子集合构建一个词典（self.dict），并将每个单词映射到唯一的索引值。同时，它还生成一个反向字典（self.inversed_dict），用于后续从索引值还原为单词。
        :param sentences:[[word1,word2,word3],[word1,word3,wordn..],...]
        :param min_count: 最小出现的次数
        :param max_count: 最大出现的次数
        :param max_feature: 总词语的最大数量
        :return:
        """
        count = Counter(word for sentence in sentences for word in sentence)

        # 比最小的数量大和比最大的数量小的需要
        if min_count is not None:
            count = {k: v for k, v in count.items() if v >= min_count}
        if max_count is not None:
            count = {k: v for k, v in count.items() if v <= max_count}

        # 限制最大的数量
        if isinstance(max_feature, int):
            count = sorted(list(count.items()), key=lambda x: x[1])
            if len(count) > max_feature:
                count = count[-int(max_feature) :]
            for w, _ in count:
                self.dict[w] = len(self.dict)
        else:
            for w in sorted(count.keys()):
                self.dict[w] = len(self.dict)

        self.fited = True
        # 准备一个index->word的字典
        self.inversed_dict = dict(zip(self.dict.values(), self.dict.keys()))

    def transform(self, sentence, max_len=None):
        """
        transform 方法的主要作用是将输入的句子转换为数值序列（向量）。它利用 fit 方法生成的词典，将每个单词替换为其对应的索引值。
        :param sentence:
        :param max_len:
        :return:
        """
        assert self.fited, "必须先进行fit操作"
        if max_len is not None:
            r = [self.PAD] * max_len
        else:
            r = [self.PAD] * len(sentence)
        if max_len is not None and len(sentence) > max_len:
            sentence = sentence[:max_len]
        for index, word in enumerate(sentence):
            r[index] = self.to_index(word)
        return np.array(r, dtype=np.int64)

    def inverse_transform(self, indices):
        """
        实现从数组 转化为文字
        :param indices: [1,2,3....]
        :return:[word1,word2.....]
        """
        return [self.to_word(i) for i in indices]


if __name__ == "__main__":
    w2s = Word2Sequence()
    w2s.fit([["你", "好", "么"], ["你", "好", "哦"]])

    print(w2s.dict)
    print(w2s.fited)
    print(w2s.transform(["你", "好", "嘛"]))
    print(w2s.transform(["你好嘛"], max_len=10))
    print(w2s.inverse_transform([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

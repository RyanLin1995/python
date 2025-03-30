"""词序列化模块

此模块实现了文本的词序列化功能，主要用于将文本转换为模型可处理的数字序列。
主要功能包括：
- 构建词汇表：统计词频，建立词语到索引的映射
- 文本转换：将文本转换为固定长度的数字序列
- 序列还原：将数字序列转换回文本

特殊标记：
- <UNK>: 表示未知词
- <PAD>: 表示填充词，用于将序列补齐到固定长度
"""

from collections import Counter
import numpy as np
from utils import tokenize

class WordSequence:
    """词序列化类
    
    实现了文本序列化的核心功能，包括词频统计、词汇表构建、文本转换等。
    
    属性:
        UNK_TAG (str): 未知词的标记
        PAD_TAG (str): 填充词的标记
        PAD (int): 填充词的索引值
        UNK (int): 未知词的索引值
        dict (dict): 词语到索引的映射字典
        inverse_dict (dict): 索引到词语的映射字典
        count (dict): 词频统计字典
        is_fit (bool): 是否已经进行了词频统计
    """
    UNK_TAG = "<UNK>"  # 表示未知字符
    PAD_TAG = "<PAD>"  # 填充符
    PAD = 0
    UNK = 1

    def __init__(self):
        """初始化词序列化对象
        
        初始化各个属性，包括词典、反向词典、词频统计等
        """
        self.inverse_dict = None
        self.dict = {  # 保存词语和对应的数字
            self.UNK_TAG: self.UNK,
            self.PAD_TAG: self.PAD,
        }
        self.count = {}  # 统计词频的
        self.is_fit = False

    def to_index(self, word):
        """将词语转换为索引
        
        参数:
            word (str): 待转换的词语
            
        返回:
            int: 词语对应的索引，如果词语不在词典中则返回UNK的索引
        """
        assert self.is_fit, "必须先进行fit操作"
        return self.dict.get(word, self.UNK)

    def to_word(self, index):
        """将索引转换为词语
        
        参数:
            index (int): 待转换的索引
            
        返回:
            str: 索引对应的词语，如果索引不存在则返回UNK标记
        """
        assert self.is_fit, "必须先进行fit操作"
        if index in self.inverse_dict:
            return self.inverse_dict[index]
        return self.UNK_TAG

    def fit(self, sentence):
        """统计词频
        
        对输入的句子进行词频统计，更新词频字典
        
        参数:
            sentence (List[str]): 词语列表
        """
        for word in sentence:
            self.count[word] = self.count.get(word, 0) + 1
        self.is_fit = True

    def build_vocab(self, min_count=5, max_count=None, max_features=None):
        """构建词汇表
        
        根据词频统计结果构建词典，可以通过参数控制词典的大小和词频范围
        
        参数:
            min_count (int): 最小词频阈值，词频低于此值的词将被过滤
            max_count (int): 最大词频阈值，词频高于此值的词将被过滤
            max_features (int): 词典的最大大小
        """
        # 根据词频阈值过滤词语
        if min_count is not None:
            self.count = {k: v for k, v in self.count.items() if v >= min_count}
        if max_count is not None:
            self.count = {k: v for k, v in self.count.items() if v <= max_count}

        # 限制词典大小
        if isinstance(max_features, int):
            count = sorted(list(self.count.items()), key=lambda x: x[1])
            if len(count) > max_features:
                count = count[-int(max_features):]
            for w, _ in count:
                self.dict[w] = len(self.dict)
        else:
            for w in sorted(self.count):
                self.dict[w] = len(self.dict)

        # 构建反向词典
        self.inverse_dict = dict(zip(self.dict.values(), self.dict.keys()))

    def transform(self, sentence, max_len=None):
        """将文本转换为数字序列
        
        将输入的词语列表转换为固定长度的数字序列
        
        参数:
            sentence (List[str]): 待转换的词语列表
            max_len (int): 序列的最大长度，超过此长度的部分将被截断
            
        返回:
            List[int]: 转换后的数字序列
        """
        assert self.is_fit, "必须先进行fit操作"
        if max_len is not None:
            r = [self.PAD] * max_len
        else:
            r = [self.PAD] * len(sentence)
        if max_len is not None and len(sentence) > max_len:
            sentence = sentence[:max_len]
        # 确保sentence是字符串列表
        sentence = [word if isinstance(word, str) else str(word) for word in sentence]
        for index, word in enumerate(sentence):
            r[index] = self.to_index(word)
        return np.array(r, dtype=np.int64).tolist()

    def inverse_transform(self, indices):
        """将数字序列转换回文本
        
        参数:
            indices (List[int]): 待转换的数字序列
            
        返回:
            List[str]: 转换后的词语列表
        """
        return [self.inverse_dict.get(i, self.UNK_TAG) for i in indices]

    def __len__(self):
        """返回词典大小
        
        返回:
            int: 词典中词语的数量
        """
        return len(self.dict)
"""
数据集加载和处理模块

此模块负责处理IMDB电影评论数据集，主要功能包括：
1. 加载训练集和测试集的正面/负面评论文本
2. 将文本数据转换为模型可处理的数字序列
3. 实现数据批次化处理

主要组件：
- ImdbDataset：继承自torch.utils.data.Dataset，实现数据集的基本功能
- process_data：将文本转换为数字序列
- collate_fn：数据批次化处理函数
- get_dataloader：创建数据加载器
"""

from torch.utils.data import DataLoader, Dataset
import os
import config
import utils
import torch


class ImdbDataset(Dataset):
    """IMDB数据集加载类
    
    负责加载和处理IMDB电影评论数据集，包括：
    - 加载训练集或测试集的评论文本
    - 处理文本文件路径
    - 提取评论的情感标签（正面/负面）
    
    参数:
        train (bool): True表示加载训练集，False表示加载测试集
    """
    def __init__(self, train=True):
        # 设置训练集和测试集的路径
        self.train_data_path = "data\\aclImdb\\train"
        self.test_data_path = "data\\aclImdb\\test"
        # 根据train参数选择数据集路径
        data_path = self.train_data_path if train else self.test_data_path

        # 把所有的文件名放入列表中
        temp_data_path = [data_path + "\\pos", data_path + "\\neg"]
        self.total_file_path = []  # 所有评论的文件路径
        for i in temp_data_path:
            file_name_list = os.listdir(i)
            file_path_list = [os.path.join(i, j) for j in file_name_list]
            self.total_file_path.extend(file_path_list)

    def __getitem__(self, index):
        file_path = self.total_file_path[index]

        # 获取 label
        label_str = file_path.split("\\")[-2]
        if label_str == "pos":
            label = 1
        else:
            label = 0

        # 读取文件
        with open(file_path, "r", encoding="utf-8") as f:
            file_data = utils.tokenize(f.read())

        return label, file_data

    def __len__(self):
        return len(self.total_file_path)


def process_data(texts, ws, max_len):
    """将文本转换为序列化的数字序列
    
    使用词序列化模型(WordSequence)将文本转换为固定长度的数字序列
    
    参数:
        texts (List[List[str]]): 文本列表，每个文本是一个词语列表
        ws (WordSequence): 词序列化模型实例
        max_len (int): 序列的最大长度
        
    返回:
        List[List[int]]: 转换后的数字序列列表
    """
    return [ws.transform(text, max_len=max_len) for text in texts]

def collate_fn(batch):
    """数据批次化处理函数
    
    将一个批次的数据转换为模型可以处理的格式：
    1. 分离文本数据和标签
    2. 将标签转换为张量
    3. 加载词序列化模型并处理文本数据
    4. 将文本数据转换为张量
    
    参数:
        batch: 一个批次的数据，包含(label, text)元组的列表
        
    返回:
        tuple: (texts_tensor, labels_tensor)
    """
    # 分离标签和文本数据
    label, texts = list(zip(*batch))
    # 将标签转换为长整型张量
    label = torch.LongTensor(label)
    
    # 加载词序列化模型
    import pickle
    ws = pickle.load(open("models/ws.pkl", "rb"))
    # 将文本转换为序列
    texts = process_data(texts, ws, max_len=config.max_len)
    texts = torch.LongTensor(texts)
    
    return texts, label


def get_dataloader(is_train=True):
    """创建数据加载器
    
    根据是否为训练模式创建相应的数据加载器，设置不同的批次大小和是否打乱数据
    
    参数:
        is_train (bool): True表示创建训练集的数据加载器，False表示创建测试集的数据加载器
        
    返回:
        DataLoader: PyTorch数据加载器实例
    """
    # 创建数据集实例
    dataset = ImdbDataset(train=is_train)
    # 根据模式选择批次大小
    batch_size = config.train_batch_size if is_train else config.test_batch_size
    # 创建并返回数据加载器
    return DataLoader(
        dataset, batch_size=batch_size, shuffle=is_train, collate_fn=collate_fn
    )


if __name__ == "__main__":
    for idx, (review, label) in enumerate(get_dataloader(is_train=True)):
        print(idx)
        print(review)
        print(label)
        break

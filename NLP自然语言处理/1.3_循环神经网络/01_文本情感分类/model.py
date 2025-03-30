"""情感分类模型定义模块

此模块定义了用于IMDB评论情感分类的神经网络模型，包括：
- 词嵌入层：将词序列转换为密集向量表示
- 全连接层：将词嵌入特征映射到情感类别

模型结构：
1. 词嵌入层：将词索引转换为100维的词向量
2. 展平层：将词向量序列展平为一维向量
3. 全连接层：将特征映射到2个类别（正面/负面）
4. Softmax层：输出概率分布
"""

import torch.nn as nn
import config
import torch.nn.functional as F


class ImdbModel(nn.Module):
    """IMDB评论情感分类模型
    
    一个简单的前馈神经网络，用于二分类任务（正面/负面评论）
    
    属性:
        embedding: 词嵌入层，将词索引映射为密集向量
        fc: 全连接层，将特征映射到类别概率
    """
    def __init__(self):
        """初始化模型的各个层
        
        创建词嵌入层和全连接层，设置词嵌入维度为100
        """
        super().__init__()
        # 词嵌入层，将词的索引转换为词向量
        # num_embeddings: 词表大小
        # embedding_dim: 词向量维度
        # padding_idx: 填充词的索引，这些位置的词向量在训练时不会更新
        self.embedding = nn.Embedding(
            num_embeddings=len(config.ws), embedding_dim=config.embedding_dim, padding_idx=config.ws.PAD
        )
        # 全连接层，输入维度为 max_len * embedding_dim，输出维度为2（二分类）
        # 全连接层，输入维度为 max_len * embedding_dim，输出维度为2（二分类）
        # 计算全连接层的输入维度：序列长度 * 词嵌入维度
        input_dim = config.max_len * config.embedding_dim
        self.fc = nn.Linear(input_dim, 2)

    def forward(self, input_data):
        """前向传播函数
        
        参数:
            input_data: 形状为[batch_size, max_len]的输入数据
                       batch_size: 批次大小
                       max_len: 序列最大长度
        
        返回:
            tensor: 形状为[batch_size, 2]的输出概率分布
                   表示每个样本属于正面/负面评论的概率
        """
        # 通过词嵌入层将输入的词索引转换为词向量
        # 输出形状：[batch_size, max_len, embedding_dim]
        input_embedding = self.embedding(
            input_data
        )

        # 将三维张量展平为二维张量，便于全连接层处理
        # 输出形状：[batch_size, max_len * embedding_dim]
        input_embedding_viewed = input_embedding.view(input_embedding.size(0), -1)

        # 通过全连接层映射到输出空间
        # 输出形状：[batch_size, 2]
        out = self.fc(input_embedding_viewed)
        
        # 使用log_softmax计算对数概率，用于计算交叉熵损失
        # dim=-1表示在最后一个维度上进行softmax
        return F.log_softmax(out, dim=-1)

    def __len__(self):
        """返回模型的词表大小
        
        返回:
            int: 词嵌入层的词表大小
        """
        return len(self.embedding)

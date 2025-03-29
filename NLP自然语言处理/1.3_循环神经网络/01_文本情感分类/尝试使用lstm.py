import torch
import torch.nn as nn

batch_size = 10  # 每次输入到模型中的样本数量
seq_len = 20  # 每个句子的最大长度（时间步数）
embedding_dim = 30  # 用长度为30的词向量表示一个词语
word_vocab = 100  # 词汇表大小，即词汇的数量
hidden_size = 18  # LSTM 隐藏层的维度，决定了 LSTM 输出的特征维度
num_layer = 2  # LSTM 的层数

# 使用 torch.randint 随机生成一个形状为 (batch_size, seq_len) 的张量，模拟一批句子的输入。
input_date = torch.randint(
    low=0, high=word_vocab, size=(batch_size, seq_len)
)  # 其中 low 是取值范围的下限，high 是取值范围的上限，size 是生成张量的维度。size 参数是一个元组，第一个元素是 batch 的大小，第二个元素是句子的长度。表示每个元素是 [0, word_vocab) 范围内的整数，对应词汇表中的索引

# 数据经过embedding处理
embedding = nn.Embedding(
    word_vocab, embedding_dim
)  # 将词汇表中的每个单词映射为一个固定长度的向量（这里是 30 维）。
input_data = embedding(
    input_date
)  # 经过 Embedding 层处理后的张量，形状为 (batch_size, seq_len, embedding_dim)，即每个单词被表示为一个 30 维向量

# 把embedding的输出作为lstm的输入
lstm = nn.LSTM(
    input_size=embedding_dim,  # 输入的特征维度（Embedding 后的维度，30）
    hidden_size=hidden_size,  # 隐藏层的输出维度（18）
    num_layers=num_layer,  # LSTM 的层数（2）
    batch_first=True,  # 输入和输出的维度顺序为 (batch, seq, feature)，否则默认是 (seq, batch, feature)
)  # 构造一个lstm层，输入维度为30，输出维度为18，层数为2。

output, (h_n, c_n) = lstm(
    input_data
)  # LSTM 的输出张量，形状为 (batch_size, seq_len, hidden_size)，表示每个时间步的隐藏状态
# h_n: 最后一层的隐藏状态，形状为 (num_layer, batch_size, hidden_size)
# c_n: 最后一层的细胞状态，形状与 h_n 相同

# 隐藏状态: 是 LSTM 的输出，表示当前时间步的特征。
# 细胞状态: 是 LSTM 的内部记忆，负责存储长期信息。
# 两者通过门控机制相互作用，共同完成对序列数据的建模。

# 获取最后一个时间步的数据，也就是 seq 的最后一个数据
last_output = output[:, -1, :]
# 获取最后一个隐藏层的数据
h_n = h_n[-1, :, :]

print(last_output == h_n)  # 判断最后一个时间步的数据和最后一个隐藏层的数据是否相等

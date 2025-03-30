"""配置文件：存储项目的全局配置参数

此模块包含了模型训练和测试过程中需要的各种参数设置，包括：
- 训练和测试的批次大小
- 文本序列的最大长度
- 词序列化模型的加载函数
"""

import pickle

# 训练时的批次大小，即每次训练时同时处理的样本数量
train_batch_size = 512

# 测试时的批次大小，即每次测试时同时处理的样本数量
test_batch_size = 500

# 文本序列的最大长度，超过此长度的文本将被截断
max_len = 50

# 词嵌入维度，用于设置词向量的维度大小
embedding_dim = 100

def load_ws():
    """加载词序列化模型"""
    try:
        return pickle.load(open("models/ws.pkl", "rb"))
    except FileNotFoundError:
        print("警告：models/ws.pkl 文件不存在，请先运行 main.py 生成该文件")
        return None

ws = load_ws()
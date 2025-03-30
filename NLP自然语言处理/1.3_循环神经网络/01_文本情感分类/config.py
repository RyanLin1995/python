"""
配置文件
"""

import pickle

train_batch_size = 512
test_batch_size = 500

# 确保 models/ws.pkl 文件存在
try:
    ws = pickle.load(open("models/ws.pkl", "rb"))
except FileNotFoundError:
    raise FileNotFoundError("请先运行 main.py 生成 ws.pkl 文件")

max_len = 50
import os
from word_sequence import WordSequence
from dataset import get_dataloader
import pickle
from tqdm import tqdm
import torch
import config

if __name__ == "__main__":
    ws = WordSequence()
    dl_train = get_dataloader(True)
    dl_test = get_dataloader(False)
    
    # 训练词序列化模型
    print("训练词序列化模型...")
    for texts, label in tqdm(dl_train, total=len(dl_train)):
        for sentence in texts:
            ws.fit(sentence)
    for texts, label in tqdm(dl_test, total=len(dl_test)):
        for sentence in texts:
            ws.fit(sentence)
    
    # 设置最小词频为5，最大词汇量为50000，可以有效减小模型大小
    ws.build_vocab(min_count=5, max_features=50000)
    print(f"词汇表大小: {len(ws)}")

    # 确保目录存在
    os.makedirs("models", exist_ok=True)

    # 保存模型
    print("保存词序列化模型...")
    pickle.dump(ws, open("models/ws.pkl", "wb"))
    print("词序列化模型保存完成！")
import os
from word_sequence import WordSequence
from dataset import get_dataloader
import pickle
from tqdm import tqdm

if __name__ == "__main__":
    ws = WordSequence()
    dl_train = get_dataloader(True)
    dl_test = get_dataloader(False)
    for reviews, label in tqdm(dl_train, total=len(dl_train)):
        for sentence in reviews:
            ws.fit(sentence)
    for reviews, label in tqdm(dl_test, total=len(dl_test)):
        for sentence in reviews:
            ws.fit(sentence)
    ws.build_vocab()
    print(len(ws))  # 42676

    # 确保目录存在
    os.makedirs("models", exist_ok=True)

    # 保存模型
    pickle.dump(ws, open("models/ws.pkl", "wb"))
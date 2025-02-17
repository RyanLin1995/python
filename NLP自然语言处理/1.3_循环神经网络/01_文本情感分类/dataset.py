import os
import re

import torch
from torch.utils.data import DataLoader, Dataset


def tokenize(text):
    # filters = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    filters = [
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "\(",
        "\)",
        "\*",
        "\+",
        ",",
        "-",
        "\.",
        "/",
        ":",
        ";",
        "<",
        "=",
        ">",
        "\?",
        "@",
        "\[",
        "\\",
        "\]",
        "^",
        "_",
        "`",
        "\{",
        "\|",
        "\}",
        "~",
        "\t",
        "\n",
        "\x97",
        "\x96",
        "”",
        "“",
    ]
    text = re.sub("<.*?>", " ", text, flags=re.S)
    text = re.sub("|".join(filters), " ", text, flags=re.S)
    return [i.strip().lower() for i in text.split()]


class ImdbDataset(Dataset):

    def __init__(self, train=True):
        self.train_data_path = "data/aclImdb/train"
        self.test_data_path = "data/aclImdb/test"
        data_path = self.train_data_path if train else self.test_data_path

        # 把所有的文件名放入列表中
        temp_data_path = [data_path + "/pos", data_path + "/neg"]
        self.total_file_path = []  # 所有评论的文件路劲
        for i in temp_data_path:
            file_name_list = os.listdir(i)
            file_path_list = [os.path.join(i, j) for j in file_name_list]
            self.total_file_path.extend(file_path_list)

    def __getitem__(self, index):
        file_path = self.total_file_path[index]

        # 获取 label
        label_str = file_path.split("/")[-2]
        if label_str == "pos":
            label = 1
        else:
            label = 0

        # 读取文件
        with open(file_path, "r", encoding="utf-8") as f:
            data = tokenize(f.read())

        return label, data

    def __len__(self):
        return len(self.total_file_path)


def collate_fn(batch):
    labels, texts = zip(*batch)
    # 填充文本数据到相同长度
    max_len = max(len(text) for text in texts)
    padded_texts = [text + ["<pad>"] * (max_len - len(text)) for text in texts]
    return torch.tensor(labels), padded_texts


def get_dataloader(is_train=True):
    imdb_dataset = ImdbDataset(train=is_train)
    data_loader = DataLoader(
        imdb_dataset, batch_size=3, shuffle=True, collate_fn=collate_fn
    )
    return data_loader


if __name__ == "__main__":
    for idx, (label, data) in enumerate(get_dataloader()):
        print(label, data)
        if idx > 10:
            break

"""
准备数据
"""

from torch.utils.data import DataLoader, Dataset
import os
import config
import utils


class ImdbDataset(Dataset):
    def __init__(self, train=True):
        self.train_data_path = "data\\aclImdb\\train"
        self.test_data_path = "data\\aclImdb\\test"
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


def collate_fn(batch):
    # 修改返回值顺序，确保 texts 是文本数据，label 是标签数据
    label, texts = list(zip(*batch))
    # texts = config.ws.transform(texts, max_len=config.max_len)
    # texts = torch.LongTensor(texts)
    # label = torch.LongTensor(label)
    return texts, label


def get_dataloader(is_train=True):
    dataset = ImdbDataset(train=is_train)
    batch_size = config.train_batch_size if is_train else config.test_batch_size
    return DataLoader(
        dataset, batch_size=batch_size, shuffle=is_train, collate_fn=collate_fn
    )


if __name__ == "__main__":
    for idx, (review, label) in enumerate(get_dataloader(is_train=True)):
        print(idx)
        print(review)
        print(label)
        break

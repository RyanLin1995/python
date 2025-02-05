from torch.utils.data import Dataset, DataLoader
import pandas as pd

data_path = "data/SMSSpamCollection"


class CifarDataSet(Dataset):
    def __init__(self):
        lines = open(data_path, "r").readlines()
        data = []
        for line in lines:
            line = line.strip()
            label = line.split("\t")[0]
            text = line.split("\t")[1]
            data.append((label, text))

        self.df = pd.DataFrame(data, columns=["label", "text"])

    def __getitem__(self, item):
        select_item = self.df.iloc[item]
        label = select_item["label"]
        text = select_item["text"]
        return label, text

    def __len__(self):
        return len(self.df)


if __name__ == "__main__":
    dataset = CifarDataSet()

    # for i in range(len(dataset)):
    #     label, text = dataset[i]
    #     print(label, text)

    data_loader = DataLoader(
        dataset=CifarDataSet(), batch_size=32, shuffle=True, num_workers=4
    )  # batch_size:传入数据的batch的大小，常用128,256等等; shuffle:是否打乱数据; num_workers:多线程读取数据，默认为0

    print("dataset len: {}".format(len(dataset)))  # 数据集的样本数
    print(
        "data_loader len: {}".format(len(data_loader))
    )  # 数据加载器的样本数，因为设置了batch_size=32，所以数据加载器的样本数是dataset样本数除以batch_size的整数部分

    for i, (label, text) in enumerate(data_loader):
        print(i, label, text)

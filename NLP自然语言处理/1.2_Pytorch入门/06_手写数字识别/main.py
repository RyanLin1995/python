import numpy as np
from torch import nn
from torch.optim import Adam
from torch.nn.functional import relu, log_softmax, nll_loss
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import Compose, ToTensor, Normalize

batch_size = 256  # 训练集的批量大小，即每次训练的样本数
test_batch_size = 1000


# 1. 准备数据集
def get_dataloader(bs, is_train=True):
    transform = Compose(
        [ToTensor(), Normalize((0.1307,), (0.3081,))]
    )  # Compose:将多个transform组合在一起; ToTensor:将PIL Image或numpy.ndarray转换成tensor; Normalize:将tensor归一化到[-1,1]
    mnist = MNIST(root="data", train=is_train, download=True, transform=transform)
    data_loader = DataLoader(mnist, batch_size=bs, shuffle=True, num_workers=4)
    return data_loader


# 2. 构建模型
class MnistModel(nn.Module):

    def __init__(self):
        super(MnistModel, self).__init__()
        self.fc1 = nn.Linear(1 * 28 * 28, 28)
        self.fc2 = nn.Linear(28, 10)

    def forward(self, input_data):
        """
        :param input_data: [batch_size,1,28,28]
        """
        # 1. 修改形状
        # input_data.view(-1, 1 * 28 * 28)
        x = input_data.view(input_data.size(0), 1 * 28 * 28)
        # 2.进行全连接操作
        x = self.fc1(x)
        # 3. 激活函数的处理，形状没有变化
        x = relu(x)
        # 4. 输出层
        out = self.fc2(x)

        return log_softmax(
            out, dim=1
        )  # 使用 log_softmax 函数，因为后续使用交叉熵损失函数，交叉熵损失函数的输入是 log_softmax 函数的输出


def train(model, optimizer, epoch):
    """实现训练过程"""
    data_loader = get_dataloader(bs=batch_size, is_train=True)
    for idx, (train_data, target) in enumerate(data_loader):
        train_data = train_data.to(device)
        target = target.to(device)

        optimizer.zero_grad()  # 清零梯度，防止梯度累积

        predict_data = model(train_data)  # 调用模型，得到预测值
        loss = nll_loss(predict_data, target)  # 计算损失函数，得到熵损失

        loss.backward()  # 反向传播，计算梯度
        optimizer.step()  # 更新参数

        if idx % 100 == 0:
            print("epoch:{},idx:{},loss:{}".format(epoch, idx, loss.item()))

        if idx % 100 == 0:
            torch.save(
                model.state_dict(), "./model/mnist_model.pth"
            )  # 保存模型和优化器
            torch.save(optimizer.state_dict(), "./model/mnist_optimizer.pth")


def test(model):
    """实现测试过程"""
    lost_list = []
    acc_list = []
    model.eval()  # 设置为测试模式

    data_loader = get_dataloader(bs=test_batch_size, is_train=False)
    for idx, (train_data, target) in enumerate(data_loader):
        train_data = train_data.to(device)
        target = target.to(device)
        with torch.no_grad():
            output = model(train_data)
            cur_loss = nll_loss(output, target)  # 计算损失函数，得到熵损失
            lost_list.append(cur_loss)
            pred = output.argmax(
                dim=1, keepdim=True
            )  # argmax:返回最大值的索引, keepdim:是否保持原维度, dim:维度
            cur_acc = (
                pred.eq(target).float().mean()
            )  # eq:比较两个tensor是否相等,返回bool值, mean:求平均值
            acc_list.append(cur_acc)

    print(
        "平均损失:{},平均准确率:{}".format(
            np.mean([loss.cpu().numpy() for loss in lost_list]),
            np.mean([acc.cpu().numpy() for acc in acc_list]),
        )
    )


if __name__ == "__main__":
    import torch
    import os

    print(torch.cuda.is_available())

    if torch.cuda.is_available():
        torch.cuda.set_device(0)
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    model = MnistModel().to(device)
    optimizer = Adam(model.parameters(), lr=0.01)

    if os.path.exists("model/mnist_model.pth"):
        model.load_state_dict(torch.load("model/mnist_model.pth"))  # 加载模型和优化器
        optimizer.load_state_dict(torch.load("model/mnist_optimizer.pth"))

    test(model)
    for i in range(50):  # 训练 10 轮
        train(model, optimizer, i)
        test(model)

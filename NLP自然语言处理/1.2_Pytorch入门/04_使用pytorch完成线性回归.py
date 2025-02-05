import torch
from torch import nn
from torch.optim import SGD  # 随机梯度下降优化器

x = torch.rand([500, 1])  # 创建一个形状为 [500, 1] 的张量，元素是 [0, 1) 区间内的随机数。
y = x * 3 + 0.8


class LinearRegression(nn.Module):

    def __init__(self):
        super().__init__()
        self.liner = nn.Linear(1, 1)  # 创建一个线性层，输入和输出维度均为 1

    # nn.Module 类中有一个默认的 forward 方法，但它不做任何操作。为了定义模型的具体行为（即如何处理输入数据），必须重写 forward 方法。这是 PyTorch 中定义模型的核心机制。
    def forward(self, x):  # forward 方法定义了前向传播的过程，即如何从输入计算输出
        out = self.liner(x)
        return out


if __name__ == '__main__':
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    x, y = x.to(device), y.to(device)
    model = LinearRegression().to(device)
    optimize = SGD(model.parameters(), lr=0.01)  # 创建一个 SGD 优化器，用于更新模型参数，学习率为 0.01。
    loss = nn.MSELoss()  # 创建一个均方误差损失函数

    for i in range(5000):
        y_predict = model(x)  # 使用模型进行预测
        loss_result = loss(y_predict, y)  # 计算预测值与真实值之间的损失

        # 在 PyTorch 中，默认情况下，梯度会在每次反向传播时累加到现有的梯度上，而不是覆盖它们。这意味着如果你不手动清空梯度，在每次迭代时，梯度会不断累积，导致错误的梯度值。
        optimize.zero_grad()  # 清空梯度，防止累加

        # 反向传播（Backpropagation）是神经网络训练的核心步骤之一。它通过链式法则从输出层逐层向前计算每个参数对损失函数的梯度。反向传播不仅计算了梯度，还通过网络传播了误差信息，使得每一层的参数都能根据损失函数的变化进行调整。
        loss_result.backward()  # 反向传播，计算梯度
        optimize.step()  # 更新模型参数，根据计算得到的梯度来更新模型参数，以最小化损失函数。即更新了 权重 （w） 和 偏置（b）
        if i % 100 == 0:
            print(rf"loss: {loss_result.data}, model: {model.liner.weight.data}, {model.liner.bias.data}")

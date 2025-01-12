import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 1. 准备数据
x_data = torch.rand([500, 1], device=device)  # 创建一个形状为 [500, 1] 的张量 x_data，其元素是随机生成的浮点数
y_data = x_data * 3 + 0.8  # 根据线性关系 y = 3x + 0.8 生成目标值 y_data。这里我们假设模型的真实权重为3，偏置为0.8。

# 2. 通过模型计算 y_predict
# 初始化权重 w 和偏置 b，并设置 requires_grad=True 表示这些张量需要计算梯度。
w = torch.rand([1, 1], requires_grad=True, device=device)  # 权重 w 是一个形状为 [1, 1] 的张量
b = torch.tensor([0.0], requires_grad=True, device=device)  # 偏置 b 是一个标量（形状为 [1] 的张量）

# 4. 通过反向传播更新参数
for i in range(2000):
    # 使用当前的权重 w 和偏置 b 计算预测值 y_predict
    y_predict = torch.matmul(x_data, w) + b  # torch.matmul 是矩阵乘法函数，这里用于计算 x_data 和 w 的乘积。

    # 3. 通过损失函数计算损失
    # 计算均方误差（MSE）损失
    loss = (y_data - y_predict).pow(2).mean()  # 具体来说，先计算预测值与真实值之间的差异 (y_data - y_predict)，然后平方 .pow(2)，最后取平均 .mean()

    # 检查梯度是否存在，如果存在则将其清零。这是为了防止梯度累积，确保每次反向传播时梯度是从零开始计算的。
    if w.grad is not None:
        w.grad.zero_()
        b.grad.zero_()

    loss.backward()  # 反向传播，自动计算所有需要梯度的张量的梯度值

    # 更新权重 w 和偏置 b，使用简单的梯度下降法。学习率设为0.01，即每次更新都减去梯度的0.01倍。
    w.data = w.data - 0.01 * w.grad
    b.data = b.data - 0.01 * b.grad

    if i % 100 == 0:
        print("w:", w.data, "b:", b.data, "loss:", loss.data)

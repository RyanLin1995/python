from torchvision.datasets import MNIST

mnist = MNIST(
    root="data", train=True, download=True
)  # 下载数据集, MNIST 是手写数字数据集
print(mnist.data.mean())

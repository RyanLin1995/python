from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split  # 数据集划分

# 1. 获取鸢尾花数据
iris = load_iris()

# 2. 对鸢尾花数据进行分割
# train_test_split 用于对数据集进行划分。一般分为
# 训练数据：用于训练，构建模型，占比 70% 80% 75%
# 测试数据：在模型检验时使用，用于评估模型是否有效，占比 30% 20% 25%

# 2.1 第一个参数是一对数组，x表示数据集的特征值，y 表示数据集的目标值
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)
# 返回值遵循的规律是训练集的特征值，测试集的特征值，训练集的目标值，测试集的目标值
print("训练集特征值:\n", x_train.shape)
print("测试集特征值:\n", x_test.shape)

# 2.2 test_size 为测试集大小，一般为 float
# x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5)
# print("训练集特征值:\n", x_train.shape)
# print("测试集特征值:\n", x_test.shape)

# 2.3 random_state 为随机数种子,不同的种子会造成不同的随机采样结果。相同的种子采样结果相同。
x_train1, x_test1, y_train1, y_test1 = train_test_split(iris.data, iris.target, test_size=0.7, random_state=22)
x_train2, x_test2, y_train2, y_test2 = train_test_split(iris.data, iris.target, test_size=0.7, random_state=22)
print("如果随机数种子一致：\n", x_train1 == x_train2)
print("如果随机数种子不一致：\n", x_train == x_train1)

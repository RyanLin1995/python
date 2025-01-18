import tensorflow as tf
import numpy as np

# 设置随机种子：为了确保每次运行代码时生成的随机数据相同，设置随机种子为42。这有助于调试和结果的可重复性。
np.random.seed(42)

# 生成随机数据
x_data = np.random.rand(500, 1).astype(np.float32)  # 使用NumPy生成500个随机数，形状为(500, 1)，并将其转换为float32类型
y_data = 3.17421 * x_data + 0.8

# 初始化权重 w 和偏置 b。使用TensorFlow的Variable来定义权重w和偏置b
w = tf.Variable(tf.random.normal([1, 1]), dtype=tf.float32)  # w是一个1x1的矩阵，初始值是从正态分布中随机抽取的
b = tf.Variable(tf.zeros([1]), dtype=tf.float32)  # b是一个1维向量，初始值为0

# 定义学习率，学习率是优化算法中用于更新权重和偏置的步长。这里设置为0.01。
learning_rate = 0.01

# 训练模型
for i in range(5000):
    with tf.GradientTape() as tape:  # 使用GradientTape记录操作：tf.GradientTape用于记录计算过程，以便后续计算梯度。with语句块中的所有操作都会被记录。
        # 计算预测值，使用矩阵乘法计算预测值y_predict，公式为y_predict = x_data * w + b。
        y_predict = tf.matmul(x_data, w) + b

        # 计算均方误差损失，公式为loss = mean((y_data - y_predict)^2)
        loss = tf.reduce_mean(tf.square(y_data - y_predict))

    # 计算梯度，使用GradientTape计算损失关于权重w和偏置b的梯度
    gradients = tape.gradient(loss, [w, b])

    # 更新权重和偏置，使用梯度下降法更新权重和偏置。assign_sub方法用于从变量中减去一个值。
    w.assign_sub(learning_rate * gradients[0])
    b.assign_sub(learning_rate * gradients[1])

    if i % 100 == 0:
        print(f"Step {i}: w = {w.numpy()}, b = {b.numpy()}, loss = {loss.numpy()}")

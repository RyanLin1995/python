import tensorflow as tf
import numpy as np

# 设置随机种子以确保可重复性
np.random.seed(42)

# 生成随机数据
x_data = np.random.rand(500, 1).astype(np.float32)
y_data = 3 * x_data + 0.8

# 初始化权重 w 和偏置 b
w = tf.Variable(tf.random.normal([1, 1]), dtype=tf.float32)
b = tf.Variable(tf.zeros([1]), dtype=tf.float32)


# 定义线性模型
def linear_model(x):
    return tf.matmul(x, w) + b


# 定义均方误差损失函数
def loss_function(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))


# 定义优化器
optimizer = tf.optimizers.SGD(learning_rate=0.01)

# 训练模型
for i in range(2000):
    with tf.GradientTape() as tape:
        y_predict = linear_model(x_data)
        loss = loss_function(y_data, y_predict)

    # 计算梯度
    gradients = tape.gradient(loss, [w, b])

    # 更新权重和偏置
    optimizer.apply_gradients(zip(gradients, [w, b]))

    if i % 100 == 0:
        print(f"Step {i}: w = {w.numpy()}, b = {b.numpy()}, loss = {loss.numpy()}")

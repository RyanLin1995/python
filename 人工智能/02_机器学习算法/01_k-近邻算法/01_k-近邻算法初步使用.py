from sklearn.neighbors import KNeighborsClassifier

# 获取数据
x = [[1], [2], [0], [0]]
y = [1, 1, 0, 0]

# 机器学习过程
# 1. 实例化一个训练模型
estimator = KNeighborsClassifier(n_neighbors=2)
# 2. 调用 fit 方法进行训练
estimator.fit(x, y)
# 3. 预测其他值
ret = estimator.predict([[-1]])  # 特征值是两个中括号
print(ret)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1.获取数据集
iris = load_iris()

# 2.数据基本处理
# 2.1 数据分割
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22, test_size=0.2)

# 3.特征工程
# 3.1 实例化一个转换器
transfer = StandardScaler()
# 3.2 调用 fit_transform 方法
x_train = transfer.fit_transform(x_train)  # 传入训练集特征值
x_test = transfer.fit_transform(x_test)  # 传入测试集特征值

# 4.机器学习(模型训练)
# 4.1 实例化一个预估器
estimator = KNeighborsClassifier(n_neighbors=5)
# 4.2 模型训练
estimator.fit(x_train, y_train)  # 传入训练集特征值和训练集目标值

# 5.模型评估
# 5.1 输出预测值
y_pre = estimator.predict(x_test)
print("预测值是:", y_pre)
print("预测值和真实值对比:", y_pre == y_test)

# 5.2 评估准确值
ret = estimator.score(x_test, y_test)
print("准确率是:", ret)

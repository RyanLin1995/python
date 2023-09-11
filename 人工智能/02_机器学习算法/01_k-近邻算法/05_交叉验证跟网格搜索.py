from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV  # tag::网格搜索
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

# tag::网格搜索
# 4.2 调用交叉验证网格搜索模型
param_grid = {'n_neighbors': [1, 3, 5, 7, 9]}
# 第一个参数为 estimator，即评估器的实例。
# param_grid 为估计器参数，是一个字典，key 为参数名称，value 为参数列表
# cv 是指定几折交叉验证
# n_jobs 是指定多少核运行
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=10, n_jobs=-1)
# end::网格搜索

# 4.3 模型训练
estimator.fit(x_train, y_train)  # 传入训练集特征值和训练集目标值

# 5.模型评估
# 5.1 输出预测值
y_pre = estimator.predict(x_test)
print("预测值是:", y_pre)
print("预测值和真实值对比:", y_pre == y_test)

# 5.2 评估准确值
ret = estimator.score(x_test, y_test)
print("准确率是:", ret)

# tag::网格搜索
# 5.3 其他评价指标
print('最好的模型：', estimator.best_estimator_)
print('最好的结果：', estimator.best_score_)
print('整体模型结果：', estimator.cv_results_)

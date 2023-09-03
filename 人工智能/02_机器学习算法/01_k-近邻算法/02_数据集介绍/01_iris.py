from sklearn.datasets import load_iris, fetch_20newsgroups  # sklearn.datasets 用于加载获取流行数据集

# 1. 数据集获取
# 1.1 datasets.load_*() 获取小规模数据集，数据包含在 datasets 里
iris = load_iris()  # 获取鸢尾花数据集

# 1.2 datasets.fetch_*(data_home=None) 获取大规模数据集，需要从网络上下载，函数的第一个参数是 data_home，表示数据集下载的目录,默认是 ~/scikit_learn_data/
news = fetch_20newsgroups()  # subset：'train' 或者 'test'，'all'，可选，选择要加载的数据集。训练集的“训练”，测试集的“测试”，两者的“全部”

# 2. 数据集属性描述
# load 和 fetch 返回的数据类型为 datasets.base.Bunch(字典格式)
# - data：特征数据数组，是 [n_samples * n_features] 的二维 numpy.ndarray 数组
# - target：标签数组，是 n_samples 的一维 numpy.ndarray 数组
# - DESCR：数据描述
# - feature_names：特征名,新闻数据，手写数字、回归数据集没有
# - target_names：标签名
print("鸢尾花数据集的返回值：\n", iris)
# 返回值是一个继承自字典的Bench
print("鸢尾花的特征值:\n", iris["data"])
print("鸢尾花的目标值：\n", iris.target)
print("鸢尾花特征的名字：\n", iris.feature_names)
print("鸢尾花目标值的名字：\n", iris.target_names)
print("鸢尾花的描述：\n", iris.DESCR)

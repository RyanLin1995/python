import numpy as np
import pandas as pd


def data_split(data_path, x=0.8, random=False):
    """
    切分数据集， 这里为了保证用户数量保持不变，将每个用户的评分数据按比例进行拆分
    :param data_path: 数据集路径
    :param x: 训练集的比例，如x=0.8，则0.2是测试集
    :param random: 是否随机切分，默认False
    :return: 用户-物品评分矩阵
    """
    print("开始切分数据集...")
    # 设置要加载的数据字段的类型
    dtype = {"userId": np.int32, "movieId": np.int32, "rating": np.float32}
    # 加载数据，我们只用前三列数据，分别是用户ID，电影ID，已经用户对电影的对应评分
    ratings = pd.read_csv(data_path, dtype=dtype, usecols=range(3))

    testset_index = []
    # 为了保证每个用户在测试集和训练集都有数据，因此按userId聚合
    for uid in ratings.groupby("userId").any().index:
        user_rating_data = ratings.where(ratings["userId"] == uid).dropna()
        if random:
            # 因为不可变类型不能被 shuffle方法作用，所以需要强行转换为列表
            index = list(user_rating_data.index)
            np.random.shuffle(index)  # 打乱列表
            _index = round(len(user_rating_data) * x)
            testset_index += list(index[_index:])
        else:
            # 将每个用户的x比例的数据作为训练集，剩余的作为测试集
            index = round(len(user_rating_data) * x)
            testset_index += list(user_rating_data.index.values[index:])

    testset = ratings.loc[testset_index]
    trainset = ratings.drop(testset_index)
    print("完成数据集切分...")
    return trainset, testset


def accuray(predict_results, method="all"):
    """
    准确性指标计算方法
    :param predict_results: 预测结果，类型为容器，每个元素是一个包含uid,iid,real_rating,pred_rating的序列
    :param method: 指标方法，类型为字符串，rmse或mae，否则返回两者rmse和mae
    :return:
    """

    def rmse(predict_results):
        """
        rmse评估指标
        :param predict_results:
        :return: rmse
        """
        length = 0
        _rmse_sum = 0
        for uid, iid, real_rating, pred_rating in predict_results:
            length += 1
            _rmse_sum += (pred_rating - real_rating) ** 2
        return round(np.sqrt(_rmse_sum / length), 4)

    def mae(predict_results):
        """
        mae评估指标
        :param predict_results:
        :return: mae
        """
        length = 0
        _mae_sum = 0
        for uid, iid, real_rating, pred_rating in predict_results:
            length += 1
            _mae_sum += abs(pred_rating - real_rating)
        return round(_mae_sum / length, 4)

    def rmse_mae(predict_results):
        """
        rmse和mae评估指标
        :param predict_results:
        :return: rmse, mae
        """
        length = 0
        _rmse_sum = 0
        _mae_sum = 0
        for uid, iid, real_rating, pred_rating in predict_results:
            length += 1
            _rmse_sum += (pred_rating - real_rating) ** 2
            _mae_sum += abs(pred_rating - real_rating)
        return round(np.sqrt(_rmse_sum / length), 4), round(_mae_sum / length, 4)

    if method.lower() == "rmse":
        rmse(predict_results)
    elif method.lower() == "mae":
        mae(predict_results)
    else:
        return rmse_mae(predict_results)


class BaselineCFBySGD(object):

    def __init__(self, number_epochs, alpha, reg, columns=None):
        # 梯度下降最高迭代次数
        self.number_epochs = number_epochs
        # 学习率
        self.alpha = alpha
        # 正则参数
        self.reg = reg
        # 数据集中user-item-rating字段的名称
        if columns is None:
            self.columns = ["uid", "iid", "rating"]
        else:
            self.columns = columns

    def fit(self, dataset):
        """
        :param dataset: uid, iid, rating
        """
        self.dataset = dataset
        # 用户评分数据
        self.users_ratings = dataset.groupby(self.columns[0]).agg([list])[[self.columns[1], self.columns[2]]]
        # 物品评分数据
        self.items_ratings = dataset.groupby(self.columns[1]).agg([list])[[self.columns[0], self.columns[2]]]
        # 计算全局平均分
        self.global_mean = self.dataset[self.columns[2]].mean()
        # 调用sgd方法训练模型参数
        self.bu, self.bi = self.sgd()

    def sgd(self):
        """
        利用随机梯度下降，优化bu，bi的值
        :return: bu, bi
        """
        # 初始化bu、bi的值，全部设为0
        bu = dict(zip(self.users_ratings.index, np.zeros(len(self.users_ratings))))
        bi = dict(zip(self.items_ratings.index, np.zeros(len(self.items_ratings))))

        for i in range(self.number_epochs):
            print("iter%d" % i)
            for uid, iid, real_rating in self.dataset.itertuples(index=False):
                error = real_rating - (self.global_mean + bu[uid] + bi[iid])

                bu[uid] += self.alpha * (error - self.reg * bu[uid])
                bi[iid] += self.alpha * (error - self.reg * bi[iid])

        return bu, bi

    def predict(self, uid, iid):
        """评分预测"""
        if iid not in self.items_ratings.index:
            raise Exception(
                "无法预测用户<{uid}>对电影<{iid}>的评分，因为训练集中缺失<{iid}>的数据".format(uid=uid, iid=iid))

        predict_rating = self.global_mean + self.bu[uid] + self.bi[iid]
        return predict_rating

    def test(self, testset):
        """预测测试集数据"""
        for uid, iid, real_rating in testset.itertuples(index=False):
            try:
                pred_rating = self.predict(uid, iid)
            except Exception as e:
                print(e)
            else:
                yield uid, iid, real_rating, pred_rating


if __name__ == '__main__':
    train_set, test_set = data_split("..\\data\\ratings.csv", random=True)

    bcf = BaselineCFBySGD(20, 0.1, 0.1, ["userId", "movieId", "rating"])
    bcf.fit(train_set)

    pred_results = bcf.test(test_set)

    rmse, mae = accuray(pred_results)

    print("rmse: ", rmse, "mae: ", mae)

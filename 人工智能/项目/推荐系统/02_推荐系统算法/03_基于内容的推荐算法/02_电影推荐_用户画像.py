import collections
from functools import reduce
from pathlib import Path
from pprint import pprint

import numpy as np
import pandas as pd
from gensim.models import TfidfModel


def get_movie_dataset():
    # 加载基于所有电影的标签
    # all-tags.csv来自ml-latest数据集中
    # 由于ml-latest-small中标签数据太多，因此借助其来扩充
    if Path("../data/cache/all-tags.cache").exists():
        _tags = pd.read_pickle("../data/cache/all-tags.cache")
    else:
        _tags = pd.read_csv("../data/all-tags.csv", usecols=range(1, 3)).dropna()
        _tags.to_pickle("../data/cache/all-tags.cache")
    tags = _tags.groupby("movieId").agg(list)

    # 加载电影列表数据集
    if Path("../data/cache/movies.cache").exists():
        movies = pd.read_pickle("../data/cache/movies.cache")
    else:
        movies = pd.read_csv("../data/movies.csv", index_col="movieId")
        movies.to_pickle("../data/cache/movies.cache")
    # 将类别词分开
    movies["genres"] = movies["genres"].apply(lambda x: x.split("|"))
    # 为每部电影匹配对应的标签数据，如果没有将会是NAN
    movies_index = set(movies.index) & set(tags.index)
    new_tags = tags.loc[list(movies_index)]
    ret = movies.join(new_tags)

    # 构建电影数据集，包含电影Id、电影名称、类别、标签四个字段
    # 如果电影没有标签数据，那么就替换为空列表
    # map(fun,可迭代对象)
    movie_dataset = pd.DataFrame(
        map(
            lambda x: (x[0], x[1], x[2], x[2] + x[3]) if x[3] is not np.nan else (x[0], x[1], x[2], []),
            ret.itertuples())
        , columns=["movieId", "title", "genres", "tags"]
    )

    movie_dataset.set_index("movieId", inplace=True)
    return movie_dataset


def create_movie_profile(movie_dataset):
    """
    使用tfidf，分析提取topn关键词
    :param movie_dataset:
    :return:
    """
    dataset = movie_dataset["tags"].values

    from gensim.corpora import Dictionary
    # 根据数据集建立词袋，并统计词频，将所有词放入一个词典，使用索引进行获取
    dct = Dictionary(dataset)
    # 根据将每条数据，返回对应的词索引和词频
    corpus = [dct.doc2bow(line) for line in dataset]
    # 训练TF-IDF模型，即计算TF-IDF值
    model = TfidfModel(corpus)

    _movie_profile = []
    for i, data in enumerate(movie_dataset.itertuples()):
        mid = data[0]
        title = data[1]
        genres = data[2]
        # 根据每条数据返回向量
        vector = model[corpus[i]]
        # 按照TF-IDF值得到top-n的关键词
        movie_tags = sorted(vector, key=lambda x: x[1], reverse=True)[:30]
        # 根据关键词提取对应的名称
        topN_tags_weights = dict(map(lambda x: (dct[x[0]], x[1]), movie_tags))
        # 将类别词的添加进去，并设置权重值为1.0
        for g in genres:
            topN_tags_weights[g] = 1.0
        topN_tags = [i[0] for i in topN_tags_weights.items()]
        _movie_profile.append((mid, title, topN_tags, topN_tags_weights))

    movie_profile = pd.DataFrame(_movie_profile, columns=["movieId", "title", "profile", "weights"])
    movie_profile.set_index("movieId", inplace=True)
    return movie_profile


def create_user_profile():
    """
    user profile画像建立：
    1. 提取用户观看列表
    2. 根据观看列表和物品画像为用户匹配关键词，并统计词频
    3. 根据词频排序，最多保留TOP-k个词，这里K设为100，作为用户的标签
    """
    if Path("../data/cache/ratings.cache").exists():
        watch_record = pd.read_pickle("../data/cache/ratings.cache")
    else:
        watch_record = pd.read_csv("../data/ratings.csv", usecols=range(2),
                                   dtype={"userId": np.int32, "movieId": np.int32})
        watch_record.to_pickle("../data/cache/ratings.cache")

    watch_record = watch_record.groupby("userId").agg(list)
    # print(watch_record)

    movie_dataset = get_movie_dataset()
    movie_profile = create_movie_profile(movie_dataset)

    user_profile = {}
    for uid, mids in watch_record.itertuples():
        # 从电影关键词权重数据中取出当前用户看过的所有电影
        record_movie_prifole = movie_profile.loc[list(mids)]
        counter = collections.Counter(reduce(lambda x, y: list(x) + list(y), record_movie_prifole["profile"].values))
        # 兴趣词
        interest_words = counter.most_common(50)
        maxcount = interest_words[0][1]
        # 计算权重
        interest_words = [(w, round(c / maxcount, 4)) for w, c in interest_words]
        user_profile[uid] = interest_words

    return user_profile


if __name__ == '__main__':
    user_profile = create_user_profile()
    pprint(user_profile)

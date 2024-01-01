import collections
from functools import reduce
from pathlib import Path

import numpy as np
import pandas as pd
from gensim.models import TfidfModel

'''
- 利用tags.csv中每部电影的标签作为电影的候选关键词
- 利用TF·IDF计算每部电影的标签的tfidf值，选取TOP-N个关键词作为电影画像标签
- 并将电影的分类词直接作为每部电影的画像标签
'''


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


def create_inverted_table(movie_profile):
    """
    建立tag-物品的倒排索引
    """
    inverted_table = {}
    for mid, weights in movie_profile["weights"].items():
        for tag, weight in weights.items():
            # 到inverted_table dict 用tag作为Key去取值 如果取不到就返回[]
            _ = inverted_table.get(tag, [])
            _.append((mid, weight))
            inverted_table.setdefault(tag, _)
    return inverted_table


def create_user_profile(movie_dataset):
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
    movie_dataset = get_movie_dataset()
    user_profile = create_user_profile(movie_dataset)
    movie_profile = create_movie_profile(movie_dataset)
    inverted_table = create_inverted_table(movie_profile)

    # 为用户产生TOP-N推荐结果
    # for uid, interest_words in user_profile.items():
    #     result_table = {}  # 电影id:[0.2,0.5,0.7]
    #     for interest_word, interest_weight in interest_words:
    #         related_movies = inverted_table[interest_word]
    #         for mid, related_weight in related_movies:
    #             _ = result_table.get(mid, [])  # mid：电影id，列表是评分的列表
    #             _.append(interest_weight)  # 只考虑用户的兴趣程度
    #             # _.append(related_weight)    # 只考虑兴趣词与电影的关联程度
    #             # _.append(interest_weight*related_weight)    # 二者都考虑
    #             result_table.setdefault(mid, _)
    #
    #     rs_result = map(lambda x: (x[0], sum(x[1])), result_table.items())
    #     rs_result = sorted(rs_result, key=lambda x: x[1], reverse=True)[:100]
    #     print(uid)
    #     pprint(rs_result)
    #     break

    # 历史数据  ==>  历史兴趣程度 ==>  历史推荐结果       离线推荐    离线计算
    # 在线推荐 ===>    娱乐(王思聪)   ===>   我 ==>  王思聪 100%
    # 近线：最近1天、3天、7天           实时计算

    # 物品冷启动——Doc2Vec Doc2Vec是建立在Word2Vec上的，用于直接计算以文档为单位的文档向量，这里我们将一部电影的所有标签词，作为整个文档，这样可以计算出每部电影的向量，通过计算向量之间的距离，来判断用于计算电影之间的相似程度。
    # import logging
    # from gensim.models.doc2vec import Doc2Vec, TaggedDocument
    #
    # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #
    # documents = [TaggedDocument(words, [movie_id]) for movie_id, words in movie_profile["profile"].items()]
    #
    # # 训练模型并保存 Doc2Vec 通过向量来表示一篇文档，一篇文档对应一个电影。向量的相似度代表了电影的相似程度
    # model = Doc2Vec(documents, vector_size=100, window=3, min_count=1, workers=4, epochs=20)  # window表示一次看多少个词
    # from gensim.test.utils import get_tmpfile
    #
    # fname = get_tmpfile("my_doc2vec_model")
    # model.save(fname)
    #
    # words = movie_profile["profile"].loc[6]
    # print(words)
    # inferred_vector = model.infer_vector(words)  # 传入电影的标签找到电影文档所对应的向量
    # # 通过docvecs找到传入的向量最相似的 n 个向量每一个向量代表了一个电影
    # sims = model.docvecs.most_similar([inferred_vector], topn=10)
    # print(sims)

    # 物品冷启动——word2vec word2vec 算法可以计算出每个词语的一个词向量，我们可以用它来表示该词的语义层面的含义
    import gensim, logging

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    sentences = movie_profile["profile"].to_list()

    model = gensim.models.Word2Vec(sentences, window=3, min_count=1, epochs=20)

    while True:
        words = input("words: ")  # action
        ret = model.wv.most_similar(positive=[words], topn=10)
        print(ret)

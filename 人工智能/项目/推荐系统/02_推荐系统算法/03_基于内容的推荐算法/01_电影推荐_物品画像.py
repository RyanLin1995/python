import numpy as np
import pandas as pd

'''
- 利用tags.csv中每部电影的标签作为电影的候选关键词
- 利用TF·IDF计算每部电影的标签的tfidf值，选取TOP-N个关键词作为电影画像标签
- 并将电影的分类词直接作为每部电影的画像标签
'''


def get_movie_dataset():
    # 加载基于所有电影的标签
    # all-tags.csv来自ml-latest数据集中
    # 由于ml-latest-small中标签数据太多，因此借助其来扩充
    _tags = pd.read_csv("../data/all-tags.csv", usecols=range(1, 3)).dropna()
    tags = _tags.groupby("movieId").agg(list)

    # 加载电影列表数据集
    movies = pd.read_csv("../data/movies.csv", index_col="movieId")
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


if __name__ == '__main__':
    movie_dataset = get_movie_dataset()
    print(movie_dataset)

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:14:39 2018

@author: CT
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 10:51:16 2018

@author: CT
"""

import jieba
from string import punctuation
from gensim.corpora import Dictionary
from gensim import matutils

add_punc = '，。、【 】 “”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥'
all_punc = punctuation + add_punc


def readDoc(doc_name):
    with open(doc_name) as f:
        doc_content = f.read()
        doc_content = doc_content.replace("\n", "")
        for i in doc_content:
            if i in all_punc:
                doc_content = doc_content.replace(i, "")
        f.close()
    return doc_content


raw_doc = []
for i in ["../../../data/txt/shadow.txt", "../../../data/txt/nahan.txt", "../../../data/txt/yukikuni.txt"]:
    raw_doc.append(readDoc(i))
texts = [[word for word in jieba.cut(doc)] for doc in raw_doc]

# 存储分词结果
dictionary = Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
# 转换为稀疏矩阵
DTM = matutils.corpus2csc(corpus)

# 本书刊登内容如下
# 构建TF-IDF的词袋
from gensim import models

# 此处省略了前面构建语料库的部分
# 生成TF-IDF模型
tfidf_model = models.TfidfModel(corpus, normalize=True)  # 用于将语料库列表转换为 TF-IDF值的对象。normalize 为 True 时使用 L2 范数进行归一化

# 对语料库应用TF-IDF
corpus_tfidf = tfidf_model[corpus]
word_matrix = matutils.corpus2csc(corpus_tfidf)
# 查看稀疏矩阵
print(word_matrix.todense())

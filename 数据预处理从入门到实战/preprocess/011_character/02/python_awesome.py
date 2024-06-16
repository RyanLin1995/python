import os
import jieba
from string import punctuation
from gensim.corpora import Dictionary
from gensim import matutils
os.chdir("C:\\Users\\Administrator\\Desktop\\awesomebook-master\\awesomebook-master")
add_punc='，。、【 】 ""：；（）《》''{} ？！⑦ ()、%^>℃：.""^-——=&#@ ￥'
all_punc=punctuation+add_punc
def readDoc(doc_name):
    with open(doc_name) as f:
        doc_content=f.read()
        doc_content=doc_content.replace("\n","")
        for i in doc_content:
            if i in all_punc:
                doc_content=doc_content.replace(i,"")
        f.close()
    return doc_content
raw_doc=[]
for i in ["data/txt/shadow.txt","data/txt/nahan.txt","data/txt/yukikuni.txt"]:
    raw_doc.append(readDoc(i))
texts=[[word for word in jieba.cut(doc) ] for doc in raw_doc]
# 存储分词结果
dictionary=Dictionary(texts)
# 创建词袋
corpus = [dictionary.doc2bow(text) for text in texts]
# 转换为稀疏矩阵
DTM=matutils.corpus2csc(corpus)

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:08:44 2018

@author: CT
"""

import os
import jieba
from string import punctuation
from gensim.corpora import Dictionary
from gensim import matutils

os.chdir("C:\\Users\\CT\\Desktop\\翻译12.22\\翻译12.21\\翻译\\译稿\\chapter11_code\\011_character\\03")
add_punc='，。、【 】 “”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥'
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
# 传入CountVectorizer前需要转换成以空格分隔的字符串
texts=[" ".join(jieba.cut(doc)) for doc in raw_doc]

# 本书刊登内容如下
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# 此处texts形式如：["word1 word2 word3", "word4 word2 word1"]
# 省略了语料库的构建部分（见源代码）
vectorizer=TfidfVectorizer(texts)
vec_fit=vectorizer.fit_transform(texts)
# 查看字典
vectorizer.vocabulary_
# 查看词袋
vec_fit
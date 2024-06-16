import pandas as pd
# 导入jieba中的词性标注模块
# 需要先安装jieba包。这里省略了安装步骤
import jieba.posseg as pseg
# 读入文本
with open("data/txt/shadow.txt") as f:
    string=f.read()
    f.close()
    
# 分词并进行词性标注 
words=pseg.cut(string)

# 从generate对象中提取单词及词性
lis_words=[]
for word,nature in words:
 lis_words.append({'word':word,'nature':nature})
 
# 构造dataframe
dat=pd.DataFrame(data=lis_words,columns=['word','nature'])

# 提取动词和名词
noun_adv=dat.loc[(dat['nature']=='n') | (dat['nature']=='v'),'word'].values.tolist()
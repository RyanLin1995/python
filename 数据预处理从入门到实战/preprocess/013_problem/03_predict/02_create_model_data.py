import pandas as pd
import numpy as np
# 本书以上内容省略

# 本书刊登内容如下
import psycopg2
import os
import random
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

# 使用psycopg2创建与Redshift的连接
con = psycopg2.connect(host='IP地址或主机名',
                       port=连接端口号,
                       dbname='数据库名',
                       user='连接的用户名',
                       password='连接的密码')


# 从文件中读入SQL语句
with open(os.path.dirname(__file__)+'/01_select_model_data.sql') as f:
  sql = f.read()

# 从Redshift中获取建模所用数据 
rsv_flg_logs = pd.read_sql(sql, con)

# 创建哑变量
rsv_flg_logs['is_man'] = \
  pd.get_dummies(rsv_flg_logs['sex'], drop_first=True)

# 以数值状态对分类值进行聚合，然后转换为分类型
rsv_flg_logs['age_rank'] = np.floor(rsv_flg_logs['age'] / 10) * 10
rsv_flg_logs.loc[rsv_flg_logs['age_rank'] < 20, 'age_rank'] = 10
rsv_flg_logs.loc[rsv_flg_logs['age_rank'] >= 60, 'age_rank'] = 60

# 转换为分类型
rsv_flg_logs['age_rank'] = rsv_flg_logs['age_rank'].astype('category')

# 将年龄由分类型转换为哑变量并添加
rsv_flg_logs = pd.concat(
  [rsv_flg_logs,
   pd.get_dummies(rsv_flg_logs['age_rank'], drop_first=False)],
  axis=1
)

# 根据12个种类的分类值将月份数值化
# 在有过拟合趋势时，首先怀疑这个变量
rsvcnt_m = rsv_flg_logs.groupby('month_num')['rsv_flg'].sum()
cuscnt_m = rsv_flg_logs.groupby('month_num')['customer_id'].count()
rsv_flg_logs['month_num_flg_rate'] =\
  rsv_flg_logs[['month_num', 'rsv_flg']].apply(
    lambda x: (rsvcnt_m[x[0]] - x[1]) / (cuscnt_m[x[0]] - 1), axis=1)

# 将过去1年内的住宿费总额对数化
# 这是为了在预测时体现出总额越大，总额的绝对大小越小的趋势
rsv_flg_logs['before_total_price_log'] = \
  rsv_flg_logs['before_total_price'].apply(lambda x: np.log(x / 10000 + 1))

# 切分为训练数据和验证数据

# 设置模型所用的变量名
target_log = rsv_flg_logs[['rsv_flg']]
# 删除不再需要的变量
rsv_flg_logs.drop(['customer_id', 'rsv_flg', 'sex', 'age', 'age_rank',
                   'month_num', 'before_total_price'], axis=1, inplace=True)

# 切分训练数据和验证数据，以便进行留出验证
train_data, test_data, train_target, test_target =\
  train_test_split(rsv_flg_logs, target_log, test_size=0.2)

#重设索引号
train_data.reset_index(inplace=True, drop=True)
test_data.reset_index(inplace=True, drop=True)
train_target.reset_index(inplace=True, drop=True)
test_target.reset_index(inplace=True, drop=True)

# 切分交叉验证所用的数据
row_no_list = list(range(len(train_target)))
random.shuffle(row_no_list)
k_fold = KFold(n_splits=4)

# 循环交叉验证的折数次
for train_cv_no, test_cv_no in k_fold.split(row_no_list):
  train_data_cv = train_data.iloc[train_cv_no, :]
  train_target_cv = train_target.iloc[train_cv_no, :]
  test_data_cv = train_data.iloc[test_cv_no, :]
  test_target_cv = train_target.iloc[test_cv_no, :]

  # 交叉验证建模
  # 训练数据：train_data_cv,train_target_cv
  # 测试数据:test_data_cv,test_target_cv

# 留出验证建模
# 训练数据:train_data,train_target
# 验证数据:test_data,test_target

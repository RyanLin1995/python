import pandas as pd
# 本书刊登内容如下
import psycopg2
import os
from scipy.sparse import csr_matrix

# 使用psycopg2创建与Redshift的连接
con = psycopg2.connect(host='IP地址或主机名',
                       port=连接的端口号,
                       dbname='数据库名',
                       user='连接的用户名',
                       password='连接的密码')

# 从Redshift中获取顾客的分类主数据
# 用于在计算完推荐后将索引号转换为ID
customer_category_mst = \
  pd.read_sql('SELECT * FROM work.customer_category_mst', con)

# 从Redshift中获取酒店的分类主数据
# 用于在计算完推荐后将索引号转换为ID  
hotel_category_mst = \
  pd.read_sql('SELECT * FROM work.hotel_category_mst', con)

# 从文件中导入SQL语句 
sql_path = os.path.dirname(__file__)+"/03_select_recommendation_data.sql"
with open(sql_path) as f:
  sql = f.read()

# 从Redshift中获取按顾客和酒店计算的2016年预订次数的纵向显示数据
matrix_data = pd.read_sql(sql, con)

# 使用csc_matrix并生成稀疏矩阵
recommend_matrix = csr_matrix(
  (matrix_data['rsv_cnt'],
   (matrix_data['customer_category_no'], matrix_data['hotel_category_no'])),
  shape=(customer_category_mst.shape[0], hotel_category_mst.shape[0])
)

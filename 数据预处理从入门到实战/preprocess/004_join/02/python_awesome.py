# 需要先将工作目录设置到preprocess目录所在的路径下
#import os
#os.chdir("工作路径")

from preprocess.load_data.data_loader import load_hotel_reserve
import pandas as pd
import numpy as np
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
# 用于垃圾回收(释放不必要的内存)的库
import gc

# 按small_area_name对酒店数进行统计
small_area_mst = hotel_tb \
  .groupby(['big_area_name', 'small_area_name'], as_index=False) \
  .size().reset_index()
small_area_mst.columns = ['big_area_name', 'small_area_name', 'hotel_cnt']

# 当酒店数大于或等于20时，将small_area_name作为join_area_id
# 当酒店数不足20时，将big_area_name作为join_area_id
# -1表示推荐酒店中应去除该酒店自身
small_area_mst['join_area_id'] = \
  np.where(small_area_mst['hotel_cnt'] - 1 >= 20,
           small_area_mst['small_area_name'],
           small_area_mst['big_area_name'])

# 去除不再需要的列
small_area_mst.drop(['hotel_cnt', 'big_area_name'], axis=1, inplace=True)

# 将推荐源的酒店表与small_area_mst表连接，设置join_area_id
base_hotel_mst = pd.merge(hotel_tb, small_area_mst, on='small_area_name') \
                   .loc[:, ['hotel_id', 'join_area_id']]

# 根据需要释放内存(不是必需操作，可在内存不足时进行)
del small_area_mst
gc.collect()

# 推荐候选表recommend_hotel_mst
recommend_hotel_mst = pd.concat([
  # 将small_area_name作为join_area_id而得到的推荐候选的主数据
  hotel_tb[['small_area_name', 'hotel_id']] \
    .rename(columns={'small_area_name': 'join_area_id'}, inplace=False),

  # 将big_area_name作为join_area_id而得到的推荐候选的主数据
  hotel_tb[['big_area_name', 'hotel_id']] \
    .rename(columns={'big_area_name': 'join_area_id'}, inplace=False)
])

# 由于连接时hotel_id列重复，所以需要更改列名
recommend_hotel_mst.rename(columns={'hotel_id': 'rec_hotel_id'}, inplace=True)

# 将recommend_hotel_mst与base_hotel_mst连接，加入推荐候选的信息 
# 通过query函数从推荐候选酒店中去除该酒店自身
pd.merge(base_hotel_mst, recommend_hotel_mst, on='join_area_id') \
  .loc[:, ['hotel_id', 'rec_hotel_id']] \
  .query('hotel_id != rec_hotel_id')

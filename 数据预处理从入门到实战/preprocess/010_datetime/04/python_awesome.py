import pandas as pd
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下 
# 导入timedelta所在的datetime库
import datetime

# 将reserve_datetime转换为datetime64[ns]类型
reserve_tb['reserve_datetime'] = \
  pd.to_datetime(reserve_tb['reserve_datetime'], format='%Y-%m-%d %H:%M:%S')

# 从reserve_datetime中提取date
reserve_tb['reserve_date'] = reserve_tb['reserve_datetime'].dt.date

# 将reserve_datetime加上1天
reserve_tb['reserve_datetime'] + datetime.timedelta(days=1)

# 将reserve_date加上1天
reserve_tb['reserve_date'] + datetime.timedelta(days=1)

# 将reserve_datetime加上1时
reserve_tb['reserve_datetime'] + datetime.timedelta(hours=1)

# 将reserve_datetime加上1分
reserve_tb['reserve_datetime'] + datetime.timedelta(minutes=1)

# 将reserve_datetime加上1秒
reserve_tb['reserve_datetime'] + datetime.timedelta(seconds=1)
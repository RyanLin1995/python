import pandas as pd
import pyproj
from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()


# 定义将分秒转换为度的函数
def convert_to_continuous(x):
    # 按下式计算时会产生微小误差
    # 要想计算正确的值时，可通过查看字符串的位数提取度分秒数值
    x_min = (x * 100 - int(x * 100)) * 100
    x_sec = (x - int(x) - x_min / 10000) * 100
    return int(x) + x_sec / 60 + x_min / 60 / 60

# 将分秒转换为度
customer_tb['home_latitude'] = customer_tb['home_latitude'] \
  .apply(lambda x: convert_to_continuous(x))
customer_tb['home_longitude'] = customer_tb['home_longitude'] \
  .apply(lambda x: convert_to_continuous(x))

# 获取世界坐标系（EPSG代码4326与WGS84坐标系一样）
epsg_world = pyproj.Proj('+init=EPSG:4326')

# 获取日本坐标系
epsg_japan = pyproj.Proj('+init=EPSG:4301')

# 将日本坐标系转换为世界坐标系
home_position = customer_tb[['home_longitude', 'home_latitude']] \
  .apply(lambda x:
         pyproj.transform(epsg_japan, epsg_world, x[0], x[1]), axis=1)

# 将customer_tb表中的经纬度信息更新为世界坐标系      
customer_tb['home_longitude'] = [x[0] for x in home_position]
customer_tb['home_latitude'] = [x[1] for x in home_position]

# 本书刊登内容如下
# 导入python中处理经纬度位置信息的库
import math
import pyproj

# 导入用于计算距离的库
from geopy.distance import great_circle, vincenty

# 这里省略了部分代码（到将经纬度修正为日本坐标系为止的部分）

# 将顾客主表和酒店主表连接到预订记录表
reserve_tb = \
  pd.merge(reserve_tb, customer_tb, on='customer_id', how='inner')
reserve_tb = pd.merge(reserve_tb, hotel_tb, on='hotel_id', how='inner')

# 获取家和酒店的经纬度信息
home_and_hotel_points = reserve_tb \
  .loc[:, ['home_longitude', 'home_latitude',
           'hotel_longitude', 'hotel_latitude']]

# 按WGS84标准设置赤道半径
g = pyproj.Geod(ellps='WGS84')

# 通过方位角、反方位角，用Vincenty公式计算距离
home_to_hotel = home_and_hotel_points \
  .apply(lambda x: g.inv(x[0], x[1], x[2], x[3]), axis=1)

# 获取方位角
[x[0] for x in home_to_hotel]

# 使用Vincenty公式计算距离
[x[2] for x in home_to_hotel]

# 使用Haversine公式计算距离
home_and_hotel_points.apply(
  lambda x: great_circle((x[1], x[0]), (x[3], x[2])).meters, axis=1)

# 使用Vincenty公式计算距离
home_and_hotel_points.apply(
  lambda x: vincenty((x[1], x[0]), (x[3], x[2])).meters, axis=1)


#定义Hubeny公式的函数
def hubeny(lon1, lat1, lon2, lat2, a=6378137, b=6356752.314245):
    e2 = (a ** 2 - b ** 2) / a ** 2
    (lon1, lat1, lon2, lat2) = \
      [x * (2 * math.pi) / 360 for x in (lon1, lat1, lon2, lat2)]
    w = 1 - e2 * math.sin((lat1 + lat2) / 2) ** 2
    c2 = math.cos((lat1 + lat2) / 2) ** 2
    return math.sqrt((b ** 2 / w ** 3) * (lat1 - lat2) ** 2 +
                     (a ** 2 / w) * c2 * (lon1 - lon2) ** 2)

# 使用Hubeny公式计算距离
home_and_hotel_points \
  .apply(lambda x: hubeny(x[0], x[1], x[2], x[3]), axis=1)

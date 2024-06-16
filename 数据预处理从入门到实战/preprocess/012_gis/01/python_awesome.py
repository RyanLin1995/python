from preprocess.load_data.data_loader import load_hotel_reserve
customer_tb, hotel_tb, reserve_tb = load_hotel_reserve()

# 本书刊登内容如下
import pyproj


# 定义用于将分、秒转换为度的函数
def convert_to_continuous(x):
  # 在使用下述公式计算时会产生舍入误差
  # 如果想计算准确的值，需要将其当作字符串按位提取度、分、秒数值
  x_min = (x * 100 - int(x * 100)) * 100
  x_sec = (x - int(x) - x_min / 10000) * 100
  return int(x) + x_sec / 60 + x_min / 60 / 60

# 将分、秒转换为度
customer_tb['home_latitude'] = customer_tb['home_latitude'] \
  .apply(lambda x: convert_to_continuous(x))
customer_tb['home_longitude'] = customer_tb['home_longitude'] \
  .apply(lambda x: convert_to_continuous(x))

# 获取世界坐标系（EPSG代码4326与WGS84相同）
epsg_world = pyproj.Proj('+init=EPSG:4326')

# 获取日本坐标系
epsg_japan = pyproj.Proj('+init=EPSG:4301')

# 将日本坐标系转换为世界坐标系
home_position = customer_tb[['home_longitude', 'home_latitude']] \
  .apply(lambda x:
         pyproj.transform(epsg_japan, epsg_world, x[0], x[1]), axis=1)

# 将customer_tb的经纬度更新为世界坐标系
customer_tb['home_longitude'] = [x[0] for x in home_position]
customer_tb['home_latitude'] = [x[1] for x in home_position]

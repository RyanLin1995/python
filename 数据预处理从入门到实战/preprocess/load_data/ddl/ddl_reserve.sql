-- 将生成的表名称指定为work.reserve_tb
CREATE TABLE work.reserve_tb
(
  -- 创建reserve_id列（数据类型为文本，添加非空约束）
  reserve_id TEXT NOT NULL,

  -- 创建hotel_id列（数据类型为文本，添加非空约束）
  hotel_id TEXT NOT NULL,

  -- 创建customer_id列（数据类型为文本，添加非空约束）
  customer_id TEXT NOT NULL,

  -- 创建reserve_datetime列（数据类型为timestamp时间戳）
  -- 添加非空约束
  reserve_datetime TIMESTAMP NOT NULL,

  -- 创建checkin_date列（时间类型为日期，添加非空约束）
  checkin_date DATE NOT NULL,

  -- 创建checkin_time列（数据类型为文本，添加非空约束）
  checkin_time TEXT NOT NULL,

  -- 创建checkout_date列（数据类型为日期，添加非空约束）
  checkout_date DATE NOT NULL,

  -- 创建people_num列（数据类型为整数型，添加非空约束）
  people_num INTEGER NOT NULL,

  -- 创建total_price列（数据类型为整数型，添加非空约束）
  total_price INTEGER NOT NULL,

  -- 将reserve_id列设置为主键（表中唯一标识记录的列）
  PRIMARY KEY(reserve_id),
  
  -- 将hotel_id列设置为外键（表示与其他表内容相同的列） 
  -- 外键引用的对象是hotel主表中的hotel_id
  -- 外键引用对象所在的表中必须先创建该键
  -- 外键引用对象必须是表的主键
  FOREIGN KEY(hotel_id) REFERENCES work.hotel_tb(hotel_id),

  -- 将customer_id设置为外键（表示与其它表内容相同的列）
  -- 外键引用的对象是顾客主表中的customer_id
  FOREIGN KEY(customer_id) REFERENCES work.customer_tb(customer_id)
)
--将数据的分配方法设置为KEY
DISTSTYLE KEY

-- 将checkin_date设置为分配列
DISTKEY (checkin_date);

-- 设置要加载数据表为work.reserve_tb
COPY work.reserve_tb

-- 将要加载的csv文件数据源设置为S3云服务器上的reserve.csv
FROM 's3://awesomebk/reserve.csv'

-- 设置用于访问S3的AWS认证信息
CREDENTIALS 'aws_access_key_id=XXXXX;aws_secret_access_key=XXXXX'

-- 设置要使用的地区（云服务的地区）
REGION AS 'us-east-1'

-- 由于CSV文件的第1行是列名，所以设置为忽略首行（不作为数据）
CSV IGNOREHEADER AS 1

-- 设置DATE类型的格式
DATEFORMAT 'YYYY-MM-DD'

-- 设置TIMESTAMP类型的格式
TIMEFORMAT 'YYYY-MM-DD HH:MI:SS';

SELECT
  hotel_id,

  -- 在VARIANCE函数中指定total_price，计算方差
  -- 通过COALESCE函数，在方差为NULL时将NULL替换为0
  COALESCE(VARIANCE(total_price), 0) AS price_var,

  -- 当数据条数大于或等于2时，在STDDEV函数中指定total_price，计算标准差
  COALESCE(STDDEV(total_price), 0) AS price_std

FROM work.reserve_tb
GROUP BY hotel_id
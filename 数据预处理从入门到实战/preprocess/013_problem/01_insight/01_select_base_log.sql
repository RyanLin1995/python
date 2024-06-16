SELECT
  cus.customer_id,
  cus.age,
  cus.sex,
  rsv.hotel_id,
  rsv.people_num,
  rsv.total_price
FROM work.reserve_tb rsv

-- 连接顾客信息表
INNER JOIN work.customer_tb cus
  ON rsv.customer_id = cus.customer_id

-- 设置要聚合记录的时间段
WHERE rsv.checkin_date >= '2016-01-01'
  AND rsv.checkin_date < '2017-01-01'

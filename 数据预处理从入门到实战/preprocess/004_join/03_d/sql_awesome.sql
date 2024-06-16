SELECT
	-- 获取连接源的所有数据列
  base.*,
    -- 当目标记录数为0时返回0，当大于等于1时计算住宿费总额
  COALESCE(SUM(combine.total_price), 0) AS price_sum

-- 指定预订记录表为连接源
FROM work.reserve_tb base

-- 指定预订记录表为要连接的历史信息
LEFT JOIN work.reserve_tb combine

	-- 将customer_id相同的记录连接
  ON base.customer_id = combine.customer_id

  -- 仅将历史数据作为连接对象
  AND base.reserve_datetime > combine.reserve_datetime
  -- 仅连接过去90天内的历史数据（详见第10章）
  AND DATEADD(day, -90, base.reserve_datetime) <= combine.reserve_datetime

-- 基于作为连接源的预定记录表的所有列执行聚合处理
GROUP BY base.reserve_id, base.hotel_id, base.customer_id,
  base.reserve_datetime, base.checkin_date, base.checkin_time, base.checkout_date,
  base.people_num, base.total_price

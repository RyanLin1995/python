SELECT
  *,
  CASE WHEN
    -- 用COUNT函数统计已经计算了多少记录的合计值，并判断是否达到3条记录
    -- 用BETWEEN语句表示从往前数第2条记录至当前记录
  	COUNT(total_price) OVER
		(PARTITION BY customer_id ORDER BY reserve_datetime ROWS
		 BETWEEN 2 PRECEDING AND CURRENT ROW) = 3

  THEN
    -- 计算包含自身在内的3条记录的合计值
  	SUM(total_price) OVER
		(PARTITION BY customer_id ORDER BY reserve_datetime ROWS
		 BETWEEN 2  PRECEDING AND CURRENT ROW)

  ELSE NULL END AS price_sum

FROM work.reserve_tb

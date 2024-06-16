SELECT
	cus.customer_id,

	-- 从年月主表中获取年份
	mst.year_num,

	-- 从年月主表中获取月份
	mst.month_num,
    
    -- 如果有total_price则添加相应的total_price，没有则添加0
	SUM(COALESCE(rsv.total_price, 0)) AS total_price_month

FROM work.customer_tb cus

-- 对顾客表和年月主表执行交叉连接 
CROSS JOIN work.month_mst mst

-- 对顾客表和年月主表、预定记录表执行连接
LEFT JOIN work.reserve_tb rsv
  ON cus.customer_id = rsv.customer_id
    AND mst.month_first_day <= rsv.checkin_date
    AND mst.month_last_day >= rsv.checkin_date

-- 提取年月主表在特定时间内的数据
WHERE mst.month_first_day >= '2017-01-01'
  AND mst.month_first_day < '2017-04-01'
GROUP BY cus.customer_id, mst.year_num, mst.month_num

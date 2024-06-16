SELECT
  c_mst.customer_category_no,
  h_mst.hotel_category_no,

	-- 计算预订记录条数
  COUNT(rsv.reserve_id) AS rsv_cnt

FROM work.reserve_tb rsv

-- 与顾客的分类主数据连接
INNER JOIN work.customer_category_mst c_mst
  ON rsv.customer_id = c_mst.customer_id

--与酒店的分类主数据连接
INNER JOIN work.hotel_category_mst h_mst
  ON rsv.hotel_id = h_mst.hotel_id

-- 仅保留指定时间段内的预订记录中出现的酒店
WHERE rsv.checkin_date >= '2016-01-01'
  AND rsv.checkin_date < '2017-01-01'

GROUP BY c_mst.customer_category_no,
		     h_mst.hotel_category_no

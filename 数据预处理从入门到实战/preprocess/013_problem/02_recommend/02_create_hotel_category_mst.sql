CREATE TABLE work.hotel_category_mst AS(
  SELECT
    -- 生成分类的索引号
	  ROW_NUMBER() OVER() - 1 AS hotel_category_no,

	  hotel_id
	FROM work.reserve_tb rsv
    -- 仅保留指定时间段内的预订记录中出现的酒店
	WHERE rsv.checkin_date >= '2016-01-01'
	  AND rsv.checkin_date < '2017-01-01'

	GROUP BY hotel_id
)

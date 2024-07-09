SELECT
	*,
    -- 使用LAG函数获取往前数第2条记录的total_price，将其作为before_price
    -- 将LAG函数引用的分组指定为customer_id
    -- 将LAG函数引用的分组内的数据指定为按reserve_datetime列的时间先后排序
  LAG(total_price, 2) OVER
	(PARTITION BY customer_id ORDER BY reserve_datetime) AS before_price

FROM work.reserve_tb
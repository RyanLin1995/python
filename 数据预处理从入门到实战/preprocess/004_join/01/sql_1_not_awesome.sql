-- 将预订记录表和酒店主表全部连接
WITH rsv_and_hotel_tb AS(
	SELECT
		-- 提取所需的列
	  rsv.reserve_id, rsv.hotel_id, rsv.customer_id,
	  rsv.reserve_datetime, rsv.checkin_date, rsv.checkin_time,
		rsv.checkout_date, rsv.people_num, rsv.total_price,
	  hotel.base_price, hotel.big_area_name, hotel.small_area_name,
	  hotel.hotel_latitude, hotel.hotel_longitude, hotel.is_business

    -- 选择连接源表reserve_tb，并将表的缩略名设置为rsv
	FROM work.reserve_tb rsv

    -- 选择要连接的hotel_tb，并将表的缩略名设置为hotel
	INNER JOIN work.hotel_tb hotel
	  -- 指定连接条件，对hotel_id相同的记录进行连接
	  ON rsv.hotel_id = hotel.hotel_id
)
-- 从连接后的表中仅提取满足条件的数据
SELECT * FROM rsv_and_hotel_tb

-- 仅提取is_business为True的数据
WHERE is_business is True
  -- 仅提取people_num为1的数据
  AND people_num = 1

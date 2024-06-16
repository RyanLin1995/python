SELECT
  -- 提取所需的列
  rsv.reserve_id, rsv.hotel_id, rsv.customer_id,
  rsv.reserve_datetime, rsv.checkin_date, rsv.checkin_time, rsv.checkout_date,
  rsv.people_num, rsv.total_price,
  hotel.base_price, hotel.big_area_name, hotel.small_area_name,
  hotel.hotel_latitude, hotel.hotel_longitude, hotel.is_business

FROM work.reserve_tb rsv
JOIN work.hotel_tb hotel
  ON rsv.hotel_id = hotel.hotel_id

-- 从酒店主表中仅提取商务酒店的数据
WHERE hotel.is_business is True
  -- 从预定记录表中仅提取住宿人数为1的数据
  AND rsv.people_num = 1

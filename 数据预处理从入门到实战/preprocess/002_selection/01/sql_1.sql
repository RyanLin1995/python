SELECT
  -- 选择reserve_id列（使用AS将列名改为rsv_time）
  reserve_id AS rsv_time,

  -- 选择hotel_id列、customer_id列、reserve_datetime列
  hotel_id, customer_id, reserve_datetime,

  -- 选择checkin_date列、checkin_time列、checkout_date列
  checkin_date, checkin_time, checkout_date

FROM work.reserve_tb
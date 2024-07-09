SELECT *
FROM work.reserve_tb

-- 为了使索引起作用，也要对checkin_date执行提取操作
WHERE checkin_date BETWEEN '2016-10-10' AND '2016-10-13'
  AND checkout_date BETWEEN '2016-10-13' AND '2016-10-14'

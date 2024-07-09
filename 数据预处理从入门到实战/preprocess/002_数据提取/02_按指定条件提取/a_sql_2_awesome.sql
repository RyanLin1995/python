SELECT *
FROM work.reserve_tb

-- 提取checkin_date在2016-10-12至2016-10-13之间的数据
WHERE checkin_date BETWEEN '2016-10-12' AND '2016-10-13'

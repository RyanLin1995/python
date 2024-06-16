SELECT *
FROM work.reserve_tb

-- 用WHERE语句指定数据提取条件
-- 提取checkin_date在2016-10-12以后的数据
WHERE checkin_date >= '2016-10-12'
  
  -- 如果要指定多个条件，就在where语句后添加AND
  -- 提取checkin_date在2016-10-13以前的数据
  AND checkin_date <= '2016-10-13'

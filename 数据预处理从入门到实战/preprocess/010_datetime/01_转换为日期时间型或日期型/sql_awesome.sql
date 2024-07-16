SELECT
  -- 转换为timestamptz类型
  TO_TIMESTAMP(reserve_datetime, 'YYYY-MM-DD HH24:MI:SS')
    AS reserve_datetime_timestamptz,

  -- 转换为timestamptz后，再将其转换为timestamp
  CAST(
    TO_TIMESTAMP(reserve_datetime, 'YYYY-MM-DD HH24:MI:SS') AS TIMESTAMP
  ) AS reserve_datetime_timestamp,

  -- 将日期和时间的字符串拼接，然后转换为TIMESTAMP
  TO_TIMESTAMP(checkin_date || checkin_time, 'YYYY-MM-DD HH24:MI:SS')
    AS checkin_timestamptz,
    
  -- 将日期时间字符串转换为日期型（时刻信息在转换后删除）
  TO_DATE(reserve_datetime, 'YYYY-MM-DD HH24:MI:SS') AS reserve_date,

  -- 将日期字符串转换为日期型
  TO_DATE(checkin_date, 'YYYY-MM-DD') AS checkin_date

FROM work.reserve_tb

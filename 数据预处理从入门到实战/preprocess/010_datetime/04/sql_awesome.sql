WITH tmp_log AS(
  SELECT
    -- 将reserve_datetime转换为TIMESTAMP类型
    CAST(
      TO_TIMESTAMP(reserve_datetime, 'YYYY-MM-DD HH24:MI:SS') AS TIMESTAMP
    ) AS reserve_datetime,

    -- 将reserve_datetime转换为DATE类型
    TO_DATE(reserve_datetime, 'YYYY-MM-DD HH24:MI:SS') AS reserve_date

  FROM work.reserve_tb
)
SELECT
  -- 将reserve_datetime加上1天
  reserve_datetime + interval '1 day' AS reserve_datetime_1d,

  -- 将reserve_date加上1天
  reserve_date + interval '1 day' AS reserve_date_1d,
  
  -- 将reserve_datetime加上1时
  reserve_datetime + interval '1 hour' AS reserve_datetime_1h,

  -- 将reserve_datetime加上1分
  reserve_datetime + interval '1 minute' AS reserve_datetime_1m,

  -- 将reserve_datetime加上1秒
  reserve_datetime + interval '1 second' AS reserve_datetime_1s

FROM tmp_log

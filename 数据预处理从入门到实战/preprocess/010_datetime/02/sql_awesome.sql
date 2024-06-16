WITH tmp_log AS(
	SELECT
		CAST(
      TO_TIMESTAMP(reserve_datetime, 'YYYY-MM-DD HH24:MI:SS') AS TIMESTAMP
    ) AS reserve_datetime_timestamp,
	FROM work.reserve_tb
)
SELECT
    -- DATE类型可使用DATE_PART函数
	-- TIMESTAMPTZ类型不可使用DATE_PART函数
	-- 获取年份
	DATE_PART(year, reserve_datetime_timestamp)
	  AS reserve_datetime_year,

  -- 获取月份
	DATE_PART(month, reserve_datetime_timestamp)
	  AS reserve_datetime_month,

  -- 获取日期
	DATE_PART(day, reserve_datetime_timestamp)
	  AS reserve_datetime_day,

  -- 获取星期(0=星期天，1＝星期一)
	DATE_PART(dow, reserve_datetime_timestamp)
	  AS reserve_datetime_day,

  -- 获取时间中的时
	DATE_PART(hour, reserve_datetime_timestamp)
	  AS reserve_datetime_hour,

  -- 获取时间中的分
	DATE_PART(minute, reserve_datetime_timestamp)
	  AS reserve_datetime_minute,

  -- 获取时间中的秒
	DATE_PART(second, reserve_datetime_timestamp)
	  AS reserve_datetime_second,

  -- 转换为指定格式的字符串
	TO_CHAR(reserve_datetime_timestamp, 'YYYY-MM-DD HH24:MI:SS')
	  AS reserve_datetime_char

FROM tmp_log

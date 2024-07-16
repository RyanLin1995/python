WITH tmp_log AS(
  SELECT
    -- 将reserve_datetime转换为TIMESTAMP类型
    CAST(
      TO_TIMESTAMP(reserve_datetime, 'YYYY-MM-DD HH24:MI:SS') AS TIMESTAMP
    ) AS reserve_datetime,

    -- 将checkin_datetime转换为TIMESTAMP类型
    CAST(
      TO_TIMESTAMP(checkin_date || checkin_time, 'YYYY-MM-DD HH24:MI:SS')
      AS TIMESTAMP
    ) AS checkin_datetime

  FROM work.reserve_tb
)
SELECT
  -- 计算年份差（不考虑月及其以后的日期时间元素）
	DATEDIFF(year, reserve_datetime, checkin_datetime) AS diff_year,

  -- 获取月份差（不考虑天及其以后的日期时间元素） 
	DATEDIFF(month, reserve_datetime, checkin_datetime) AS diff_month,

  -- 下面3个不属于例题要求，仅供参考

  -- 计算天数的差值（不考虑小时及其以后的日期时间元素）
	DATEDIFF(day, reserve_datetime, checkin_datetime) AS diff_day,

  -- 计算小时数的差值（不考虑分钟及其以后的日期时间元素）
	DATEDIFF(hour, reserve_datetime, checkin_datetime) AS diff_hour,

  -- 计算分钟数的差值（不考虑秒及其以下的日期时间元素）
	DATEDIFF(minute, reserve_datetime, checkin_datetime) AS diff_minute,

  -- 以天为单位计算差值
	CAST(DATEDIFF(second, reserve_datetime, checkin_datetime) AS FLOAT) /
    (60 * 60 * 24) AS diff_day2,

  -- 以时为单位计算差值
	CAST(DATEDIFF(second, reserve_datetime, checkin_datetime) AS FLOAT) /
	  (60 * 60) AS diff_hour2,

  -- 以分为单位计算差值
  CAST(DATEDIFF(second, reserve_datetime, checkin_datetime) AS FLOAT) /
    60 AS diff_minute2,

  -- 以秒为单位计算差值
	DATEDIFF(second, reserve_datetime, checkin_datetime) AS diff_second
FROM tmp_log

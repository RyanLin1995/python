SELECT
	base.*,

  -- 添加休息日标志
  mst.holidayday_flg,

  -- 添加休息日前一天标志
  mst.nextday_is_holiday_flg

FROM work.reserve_tb base

-- 与休息日主数据连接
INNER JOIN work.holiday_mst mst
  ON base.checkin_date = mst.target_day

SELECT
	*,
  -- 用total_price除以1000，然后加上1，对结果进行对数化
  LOG(total_price / 1000 + 1) AS total_price_log

FROM work.reserve_tb

-- 计算每种产品的生产件数和故障件数
WITH type_mst AS(
	SELECT
		type,

    -- 生产件数
		COUNT(*) AS record_cnt,

    -- 故障件数
		SUM(CASE WHEN fault_flg THEN 1 ELSE 0 END) AS fault_cnt

	FROM work.production_tb
	GROUP BY type
)
SELECT
  base.*,

  -- 计算排除当前产品记录后每种产品的平均故障率
  CAST(t_mst.fault_cnt - (CASE WHEN fault_flg THEN 1 ELSE 0 END) AS FLOAT) /
    (t_mst.record_cnt - 1) AS type_fault_rate

FROM work.production_tb base
INNER JOIN type_mst t_mst
  ON base.type = t_mst.type

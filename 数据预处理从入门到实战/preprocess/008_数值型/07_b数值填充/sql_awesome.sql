SELECT
  type,
  length,

  -- 用1填充thickness的缺失值
  COALESCE(thickness, 1) AS thickness,
  fault_flg
FROM work.production_missn_tb

SELECT
  -- 生成“男性”的标志
  CASE WHEN sex = 'man' THEN TRUE ELSE FALSE END AS sex_is_man,

  -- 生成“女性”的标志
	CASE WHEN sex = 'woman' THEN TRUE ELSE FALSE END AS sex_is_woman

FROM work.customer_tb

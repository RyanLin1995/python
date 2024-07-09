-- 使用WITH语句，生成reserve_tb_random临时表
WITH reserve_tb_random AS(
  SELECT
    *,

    -- 为每个customer_id生成特定的随机数
    -- 汇总每个customer_id的随机数，并检索其中的第一个值
    FIRST_VALUE(RANDOM()) OVER (PARTITION BY customer_id) AS random_num

  FROM work.reserve_tb
)
-- “*”用于提取全部的列，如果要删除random_num列，则需要重新指定列
SELECT *
FROM reserve_tb_random

-- 采样50%，当customer_id对应的随机数小于或等于0.5时，提取该数据行
WHERE random_num <= 0.5

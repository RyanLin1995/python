WITH rsv_cnt_table AS(
  SELECT
    -- 通过Round函数进行四舍五入，将total_price转换为以1000为单位的值
    ROUND(total_price, -3) AS total_price_round,

    -- 用COUNT函数计算不同金额的预订记录数
    COUNT(*) AS rsv_cnt

  FROM work.reserve_tb
  
  -- 指定用AS新命名的列名total_price_round，并将住宿费以1000为单位进行聚合
  GROUP BY total_price_round
)
SELECT
  total_price_round
FROM rsv_cnt_table

-- 通过（）内的query语句求众数，然后用where语句提取与众数对应的total_price_round值
WHERE rsv_cnt = (SELECT max(rsv_cnt) FROM rsv_cnt_table)

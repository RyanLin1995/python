SELECT hotel_id,
       MAX(total_price)                                                                      AS price_max,
       MIN(total_price)                                                                      AS price_min,
       AVG(total_price)                                                                      AS price_avg,
       -- 使用 PERCENTILE_CONT(0.5) 计算中位数
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_price) OVER (PARTITION BY hotel_id) AS price_med,
       -- 计算第20百分位数
       PERCENTILE_CONT(0.2) WITHIN GROUP (ORDER BY total_price) OVER (PARTITION BY hotel_id) AS price_20per
FROM work.reserve_tb
GROUP BY hotel_id;
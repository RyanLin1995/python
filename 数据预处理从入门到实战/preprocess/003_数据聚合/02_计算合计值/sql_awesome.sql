SELECT
  hotel_id,
  people_num,
  
  -- 在SUM函数中指定total_price，计算住宿费总额
  SUM(total_price) AS price_sum

FROM work.reserve_tb

-- 将聚合单元指定为hotel_id和people_num的组合
GROUP BY hotel_id, people_num

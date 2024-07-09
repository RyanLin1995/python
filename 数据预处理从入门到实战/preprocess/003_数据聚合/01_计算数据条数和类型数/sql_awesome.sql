SELECT
  -- 提取聚合单元：酒店ID 
  hotel_id,

  -- 将reserve_id传入COUNT函数，计算reserve_id为非NULL的行数
  COUNT(reserve_id) AS rsv_cnt,

  -- 给customer_id添加distinct关键词，去重 
  -- 计算去重后的customer_id的行数
  COUNT(distinct customer_id) AS cus_cnt

FROM work.reserve_tb

-- 用GROUP BY语句将hotel_id指定为聚合单元
GROUP BY hotel_id

SELECT
  hotel_id,

  -- 使用RANK函数指定预订记录数的位次
  -- 指定将COUNT(*) 指定为RANK 的基准（针对聚合后的预订记录数进行排序的计算处理）
  -- 使用DESC指定降序排列
  RANK() OVER (ORDER BY COUNT(*) DESC) AS rsv_cnt_rank

FROM work.reserve_tb

-- 将hotel_id指定为聚合单元，这里是为计算预订记录数而进行的聚合指定，与RANK函数无关
GROUP BY hotel_id

SELECT
  *,

  -- 通过ROW_NUMBER获取位次
  -- 通过PARTITION by customer_id设置按顾客返回位次
  -- 通过ORDER BY reserve_datetime按预订时间的先后排序
  ROW_NUMBER()
    OVER (PARTITION BY customer_id ORDER BY reserve_datetime) AS log_no

FROM work.reserve_tb

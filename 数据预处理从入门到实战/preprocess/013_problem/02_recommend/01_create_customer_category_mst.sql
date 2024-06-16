CREATE TABLE work.customer_category_mst AS(
  SELECT
    -- 生成分类的索引号（为了使之从0开始，这里要减1）
    ROW_NUMBER() OVER() - 1 AS customer_category_no,

    customer_id
  FROM work.reserve_tb rsv
  -- 仅保留指定时间段内的预订记录中出现的顾客
  WHERE rsv.checkin_date >= '2016-01-01'
    AND rsv.checkin_date < '2017-01-01'

  GROUP BY customer_id
)
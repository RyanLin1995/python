WITH target_customer_month_log AS(
  -- 为了使数据结构易于理解，这里使用了2层with语句
  -- 对顾客主表和月份主表执行交叉连接，构造用于预测的数据
  WITH customer_month_log AS(
    SELECT
      cus.customer_id,
      cus.age,
      cus.sex,
      mst.year_num,
      mst.month_num,
      TO_DATE(mst.month_first_day, 'YYYY-MM-DD') AS month_first_day,
      TO_DATE(mst.month_last_day, 'YYYY-MM-DD') AS month_last_day
    FROM work.customer_tb cus
    CROSS JOIN work.month_mst mst
    
    -- 时间段不是2016-04-01至2017-04-01的1年的时间，还要向前延长3个月
    -- 因为稍后会将最多3个月前的预订标志添加为解释变量
    WHERE mst.month_first_day >= '2016-01-01'
      AND mst.month_first_day < '2017-04-01'
  )
  -- 连接预订记录表并添加预订标志
  -- 为了生成解释变量，后半部分会再次连接预订记录表
  -- 虽然可以将处理合在一起，但这里为了易于理解而将其分开了
  , tmp_rsvflg_log AS(
    SELECT
      base.customer_id,
      base.sex,
      base.age,
      base.year_num,
      base.month_num,
      base.month_first_day,
     
      -- 生成预订标志
      CASE WHEN COUNT(target_rsv.reserve_id) > 0 THEN 1 ELSE 0 END
        AS rsv_flg

    FROM customer_month_log base
    
    
    -- 连接与目标月份的时间段相对应的预订记录表
    LEFT JOIN work.reserve_tb target_rsv
      ON base.customer_id = target_rsv.customer_id
      AND TO_DATE(target_rsv.reserve_datetime, 'YYYY-MM-DD HH24:MI:SS')
          BETWEEN base.month_first_day AND base.month_last_day

    GROUP BY base.customer_id,
             base.sex,
             base.age,
             base.year_num,
             base.month_num,
             base.month_first_day
  )
  -- 使用LAG函数，添加此前1至3个月的预订标志
  , rsvflg_log AS(
    SELECT
      *,
      -- 往前数第1个月的预订标志
      LAG(rsv_flg, 1) OVER(PARTITION BY customer_id
                           ORDER BY month_first_day)
        AS before_rsv_flg_m1,
      -- 往前数第2个月的预订标志
      LAG(rsv_flg, 2) OVER(PARTITION BY customer_id
                           ORDER BY month_first_day)
        AS before_rsv_flg_m2,
      -- 往前数第3个月的预订标志
      LAG(rsv_flg, 3) OVER(PARTITION BY customer_id
                           ORDER BY month_first_day)
        AS before_rsv_flg_m3

    FROM tmp_rsvflg_log
  )
  -- 为了按顾客对特定月份的数据进行采样，用随机数添加排序
  , rsvflg_target_log AS(
    SELECT
      *,
      -- 用随机数计算位次
      ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY RANDOM())
        AS random_rank

    FROM rsvflg_log
    -- 提取2016年度（从2016-04-01至2017-03-31）的数据
    WHERE month_first_day >= '2016-04-01'
      AND month_first_day < '2017-04-01'
  )
  -- 利用随机数生成的位次进行随机采样
  SELECT * FROM rsvflg_target_log where random_rank = 1
)
-- 连接过去1年（365天）内的预订记录表，准备生成解释变量数据
, rsvflg_and_history_rsv_log AS(
  SELECT
    base.*,
    before_rsv.reserve_id AS before_reserve_id,
    
    -- 转换为预订日期（具体到天）
    TO_DATE(before_rsv.reserve_datetime, 'YYYY-MM-DD HH24:MI:SS')
      AS before_reserve_date,
    before_rsv.total_price AS before_total_price,

    -- 计算住宿人数为1人的标志
    CASE WHEN before_rsv.people_num = 1 THEN 1 ELSE 0 END
      AS before_people_num_1,

    -- 计算住宿人数为2人及以上的标志
    CASE WHEN before_rsv.people_num >= 2 THEN 1 ELSE 0 END
      AS before_people_num_over2,
    
    -- 计算过去的住宿月份是否为同一月份（不同年份相同月份也算同一月份）的标志
    CASE
      WHEN base.month_num =
        CAST(DATE_PART(MONTH, TO_DATE(before_rsv.reserve_datetime,
                                      'YYYY-MM-DD HH24:MI:SS')) AS INT)
        THEN 1 ELSE 0 END AS before_rsv_target_month

  FROM target_customer_month_log base
  -- 连接同一顾客过去1年（365天）内的预订记录
  LEFT JOIN work.reserve_tb before_rsv
    ON base.customer_id = before_rsv.customer_id
    AND TO_DATE(before_rsv.checkin_date, 'YYYY-MM-DD')
        BETWEEN DATEADD(DAY, -365,
                        TO_DATE(base.month_first_day, 'YYYY-MM-DD'))
            AND DATEADD(DAY, -1,
                        TO_DATE(base.month_first_day, 'YYYY-MM-DD'))
)
-- 对已连接的过去1年内的预订记录进行聚合，转换为解释变量
-- （也可以与前一阶段的SQL和操作合在一起）
SELECT
  customer_id,
  rsv_flg,
  sex,
  age,
  month_num,
  before_rsv_flg_m1,
  before_rsv_flg_m2,
  before_rsv_flg_m3,
  
  -- 计算过去1年内的住宿费总额（当没有预订记录时，用0填充）
  COALESCE(SUM(before_total_price), 0) AS before_total_price,
  
  -- 过去1年内的预订次数
  COUNT(before_reserve_id) AS before_rsv_cnt,

  -- 过去1年内住宿人数为1人的预订次数
  SUM(before_people_num_1) AS before_rsv_cnt_People_num_1,

  -- 过去1年内住宿人数为2人及其以上的预订次数
  SUM(before_people_num_over2) AS before_rsv_cnt_People_num_over2,
  
  -- 计算最近一次预订是多少天前
  -- 当最近没有预订记录时，用366（1年前 + 1天前 = 366天前）填充
  COALESCE(DATEDIFF(day, MAX(before_reserve_date), month_first_day), 0)
    AS last_rsv_day_diff,

  -- 计算过去1年内相同月份的预订次数
  SUM(before_rsv_target_month) AS before_rsv_cnt_target_month

FROM rsvflg_and_history_rsv_log
GROUP BY
  customer_id,
  sex,
  age,
  month_num,
  before_rsv_flg_m1,
  before_rsv_flg_m2,
  before_rsv_flg_m3,
  month_first_day,
  rsv_flg,
  month_first_day

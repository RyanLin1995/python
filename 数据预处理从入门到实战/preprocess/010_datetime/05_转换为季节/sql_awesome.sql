WITH tmp_log AS(
  SELECT
    --将reserve_datetime转换为TIMESTAMP类型并获取月份
    DATE_PART(
      month,
      CAST(
        TO_TIMESTAMP(reserve_datetime, 'YYYY-MM-DD HH24:MI:SS') AS TIMESTAMP
      )
    ) AS reserve_month

  FROM work.reserve_tb
)
SELECT
  CASE
    -- 当月份大于等于3且小于等于5时，返回spring
    WHEN 3 <= reserve_month and reserve_month <= 5 THEN 'spring'
    
    -- 当月份大于等于6且小于等于8时，返回summer
    WHEN 6 <= reserve_month and reserve_month <= 8 THEN 'summer'

    -- 当月份大于等于9且小于等于11时，返回autumn
    WHEN 9 <= reserve_month and reserve_month <= 11 THEN 'autumn'
    
    -- 当不属于以上情况时（即月份为1、2、12时），返回winter
    ELSE 'winter' END

  AS reserve_season
FROM tmp_log

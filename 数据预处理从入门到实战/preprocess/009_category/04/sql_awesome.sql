SELECT
  *,
  -- 将sex和以10岁为间隔的年龄的分类值以字符串的形式进行拼接，中间用“_”相连
  sex || '_' || CAST(FLOOR(age / 10) * 10 AS TEXT) AS sex_and_age

FROM work.customer_tb

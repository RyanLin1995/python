SELECT
  -- 转换为整数型
  -- 如果写成40000/3的形式则将其作为整数类型进行计算，小数点后面的部分不计算
  CAST((40000.0 / 3) AS INT2) AS v_int2,
  CAST((40000.0 / 3) AS INT4) AS v_int4,
  CAST((40000.0 / 3) AS INT8) AS v_int8,
  
  -- 转换为浮点型
  CAST((40000.0 / 3) AS FLOAT4) AS v_float4,
  CAST((40000.0 / 3) AS FLOAT8) AS v_float8

-- 上述内容与reserve_tb表中数据没多大关系，但为了演示这里还是在FROM中指定了表名
FROM work.reserve_tb
LIMIT 1

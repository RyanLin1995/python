SELECT *
FROM work.reserve_tb

-- 为每个数据行生成随机数，按随机数升序重新排列数据
ORDER BY RANDOM()

-- 用LIMIT语句指定采样数
-- 输入提前计算好的数据条数，乘以提取的比例，用ROUND函数四舍五入 
LIMIT ROUND(120000 * 0.5)

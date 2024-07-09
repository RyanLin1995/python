SELECT *
FROM work.reserve_tb

-- 生成随机数，仅提取小于或等于0.5的数据行
WHERE RANDOM() <= 0.5

SELECT *
FROM work.production_missn_tb

-- 删除thickness为null的记录
WHERE thickness is not NULL

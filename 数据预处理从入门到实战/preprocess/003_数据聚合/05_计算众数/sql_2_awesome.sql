SELECT
  ROUND(total_price, -3) AS total_price_round
FROM work.reserve_tb
GROUP BY total_price_round

-- 将COUNT函数计算出的不同金额的预订记录按降序排列（DESC表示降序）
ORDER BY COUNT(*) DESC

-- 使用LIMIT语句仅提取第1项
LIMIT 1

SELECT
	*,
    -- 更改为以10为增量的值 
	FLOOR(age / 10) * 10 AS age_rank

FROM work.customer_tb

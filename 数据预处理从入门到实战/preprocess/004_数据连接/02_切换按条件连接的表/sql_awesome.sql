-- 该表用于按small_area_name对酒店进行计数并生成连接键
WITH small_area_mst AS(
  SELECT
    small_area_name,

    -- 当酒店数大于或等于20时，将small_area_name作为join_area_id
    -- 当酒店数小于20时，将big_area_name作为join_area_id
    -- -1表示推荐酒店中应排除该酒店自身
    CASE WHEN COUNT(hotel_id)-1 >= 20
			THEN small_area_name ELSE big_area_name END AS join_area_id

  FROM work.hotel_tb
  GROUP BY big_area_name, small_area_name
)
-- 推荐候选表
, recommend_hotel_mst AS(
  -- 将big_area_name作为join_area_id而得到的推荐候选的主数据
  SELECT
    big_area_name AS join_area_id,
    hotel_id AS rec_hotel_id
  FROM work.hotel_tb

  -- 通过union将各表合并
  UNION
  
  -- 将small_area_name作为join_area_id而得到的推荐候选的主数据
  SELECT
    small_area_name AS join_area_id,
    hotel_id AS rec_hotel_id
  FROM work.hotel_tb
)
SELECT
  hotels.hotel_id,
  r_hotel_mst.rec_hotel_id

-- 导入推荐源表hotel_tb
FROM work.hotel_tb hotels

-- 为确定各酒店的推荐候选酒店的目标区域，连接small_area_mst
INNER JOIN small_area_mst s_area_mst
  ON hotels.small_area_name = s_area_mst.small_area_name

-- 连接目标区域的推荐候选酒店
INNER JOIN recommend_hotel_mst r_hotel_mst
  ON s_area_mst.join_area_id = r_hotel_mst.join_area_id

  -- 从推荐候选酒店中排除该酒店自身
  AND hotels.hotel_id != r_hotel_mst.rec_hotel_id

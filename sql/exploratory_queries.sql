-- 전체 리스팅 개수 확인
SELECT COUNT(*) FROM listings;

-- 자치구별 평균 가격 (전체)
SELECT neighbourhood_group, COUNT(*) AS num_listings, ROUND(AVG(price), 2) AS avg_price
FROM listings
GROUP BY neighbourhood_group
ORDER BY avg_price DESC;

-- 맨해튼 내 가격 범위 확인
SELECT MIN(price), MAX(price), AVG(price) FROM listings WHERE neighbourhood_group = 'Manhattan';

-- 맨해튼 최고가 리스팅 10개
SELECT name, room_type, price
FROM listings
WHERE neighbourhood_group = 'Manhattan'
ORDER BY price DESC
LIMIT 10;

-- 세그먼트별 평균 가격
SELECT segment, COUNT(*) AS num_listings, ROUND(AVG(price), 2) AS avg_price
FROM listings
GROUP BY segment;

-- 자치구별 평균 가격 (럭셔리 제외)
SELECT neighbourhood_group, COUNT(*) AS num_listings, ROUND(AVG(price), 2) AS avg_price
FROM listings
WHERE segment = 'mainstream'
GROUP BY neighbourhood_group
ORDER BY avg_price DESC;
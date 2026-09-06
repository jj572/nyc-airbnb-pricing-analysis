-- Total number of listings
SELECT COUNT(*) FROM listings;

-- Average price by borough (all listings)
SELECT neighbourhood_group, COUNT(*) AS num_listings, ROUND(AVG(price), 2) AS avg_price
FROM listings
GROUP BY neighbourhood_group
ORDER BY avg_price DESC;

-- Price range within Manhattan
SELECT MIN(price), MAX(price), AVG(price) FROM listings WHERE neighbourhood_group = 'Manhattan';

-- Top 10 most expensive listings in Manhattan
SELECT name, room_type, price
FROM listings
WHERE neighbourhood_group = 'Manhattan'
ORDER BY price DESC
LIMIT 10;

-- Average price by segment
SELECT segment, COUNT(*) AS num_listings, ROUND(AVG(price), 2) AS avg_price
FROM listings
GROUP BY segment;

-- Average price by borough, excluding luxury segment
SELECT neighbourhood_group, COUNT(*) AS num_listings, ROUND(AVG(price), 2) AS avg_price
FROM listings
WHERE segment = 'mainstream'
GROUP BY neighbourhood_group
ORDER BY avg_price DESC;
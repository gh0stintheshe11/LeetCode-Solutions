# Write your MySQL query statement below
SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING SUM(price) = (
    SELECT MAX(total_sales)
    FROM (
        SELECT SUM(price) AS total_sales
        FROM Sales
        GROUP BY seller_id
    ) AS subquery
);
# Write your MySQL query statement below
SELECT DISTINCT buyer_id
FROM Sales
WHERE product_id = (SELECT product_id FROM Product WHERE product_name = 'S8')
AND buyer_id NOT IN (
    SELECT buyer_id 
    FROM Sales 
    WHERE product_id = (SELECT product_id FROM Product WHERE product_name = 'iPhone')
);
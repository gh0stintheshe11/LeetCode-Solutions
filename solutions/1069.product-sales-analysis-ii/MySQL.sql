# Write your MySQL query statement below
SELECT
    p.product_id,
    SUM(s.quantity) AS total_quantity
FROM
    Sales s
JOIN
    Product p ON s.product_id = p.product_id
GROUP BY
    p.product_id;
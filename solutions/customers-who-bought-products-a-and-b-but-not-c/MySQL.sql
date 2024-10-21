SELECT c.customer_id, c.customer_name
FROM Customers c
JOIN (
    SELECT customer_id
    FROM Orders
    WHERE product_name IN ('A', 'B', 'C')
    GROUP BY customer_id
    HAVING COUNT(DISTINCT product_name) = 2 AND
           SUM(product_name = 'C') = 0
) o ON c.customer_id = o.customer_id
ORDER BY c.customer_id;
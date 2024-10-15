SELECT customer_id, product_id, product_name
FROM (
    SELECT o.customer_id, o.product_id, p.product_name, 
           RANK() OVER (PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rank_order
    FROM Orders o
    JOIN Products p ON o.product_id = p.product_id
    GROUP BY o.customer_id, o.product_id
) ranked
WHERE rank_order = 1;
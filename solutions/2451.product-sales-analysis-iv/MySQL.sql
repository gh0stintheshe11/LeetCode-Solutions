WITH cte AS (
    SELECT  
        t1.user_id, t1.product_id, SUM(t1.quantity * t2.price) AS total
    FROM sales AS t1 
    INNER JOIN product AS t2 
    ON t1.product_id = t2.product_id 
    GROUP BY t1.user_id, t2.product_id
)

SELECT user_id, product_id 
FROM (
    SELECT *, DENSE_RANK() OVER (PARTITION BY user_id ORDER BY total DESC) AS ranking
    FROM cte
) AS t4 
WHERE ranking = 1;
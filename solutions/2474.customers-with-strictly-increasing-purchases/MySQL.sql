WITH T1 AS (
    SELECT *,
           EXTRACT(Year FROM order_date) - LAG(EXTRACT(Year FROM order_date)) OVER(PARTITION BY customer_id ORDER BY order_date ASC) AS year_diff 
    FROM Orders
),
T2 AS (
    SELECT *,
           EXTRACT(Year FROM order_date) AS yr 
    FROM T1 
    WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM T1 WHERE year_diff > 1)
),
T3 AS (
    SELECT customer_id, yr, SUM(price) AS price 
    FROM T2 
    GROUP BY customer_id, yr
),
T4 AS (
    SELECT *, price - LAG(price) OVER(PARTITION BY customer_id ORDER BY yr ASC) AS price_diff 
    FROM T3
)

SELECT DISTINCT customer_id  
FROM T4
WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM T4 WHERE price_diff <= 0)
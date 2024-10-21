WITH cte1 AS (
    SELECT a.customer_id, a.transaction_date
    FROM Transactions a, Transactions b
    WHERE a.customer_id = b.customer_id AND b.amount > a.amount AND DATEDIFF(b.transaction_date, a.transaction_date) = 1
),
cte2 AS (
    SELECT customer_id, transaction_date, 
           DAYOFYEAR(transaction_date) - ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY transaction_date) gap
    FROM cte1
),
cte3 AS (
    SELECT customer_id, gap, MIN(transaction_date) AS consecutive_start, COUNT(*) AS consecutive_days
    FROM cte2
    GROUP BY 1, 2
    HAVING COUNT(*) >= 2
)
SELECT customer_id, consecutive_start, DATE_ADD(consecutive_start, INTERVAL consecutive_days DAY) consecutive_end
FROM cte3
ORDER BY 1
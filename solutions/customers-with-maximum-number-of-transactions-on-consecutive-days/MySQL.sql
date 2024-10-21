WITH cte AS (
    SELECT
        customer_id,
        transaction_date,
        row_number() OVER (PARTITION BY customer_id ORDER BY transaction_date) AS rnk
    FROM
        transactions
),

A AS (
    SELECT *,
    DATE_SUB(transaction_date, INTERVAL rnk DAY) AS grp
    FROM cte
),

B AS (
    SELECT grp, customer_id, COUNT(*) AS cons
    FROM A
    GROUP BY 1, 2
)

SELECT customer_id FROM B WHERE cons = (SELECT MAX(cons) FROM B)
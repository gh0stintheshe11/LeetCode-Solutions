WITH customer_data AS (
    SELECT 
        t.customer_id,
        SUM(t.amount) AS total_amount,
        COUNT(*) AS transaction_count,
        COUNT(DISTINCT p.category) AS unique_categories,
        ROUND(SUM(t.amount) / COUNT(*), 2) AS avg_transaction_amount
    FROM 
        Transactions t
    JOIN 
        Products p ON t.product_id = p.product_id
    GROUP BY 
        t.customer_id
),
top_category_data AS (
    SELECT 
        t.customer_id,
        p.category,
        DENSE_RANK() OVER (PARTITION BY t.customer_id ORDER BY COUNT(*) DESC, MAX(t.transaction_date) DESC) AS rk
    FROM 
        Transactions t
    JOIN 
        Products p ON t.product_id = p.product_id
    GROUP BY 
        t.customer_id, p.category
)
SELECT 
    cd.customer_id,
    ROUND(cd.total_amount, 2) AS total_amount,
    cd.transaction_count,
    cd.unique_categories,
    cd.avg_transaction_amount,
    (SELECT category FROM top_category_data tcd WHERE tcd.customer_id = cd.customer_id AND rk = 1 LIMIT 1) AS top_category,
    ROUND(cd.transaction_count * 10 + cd.total_amount / 100, 2) AS loyalty_score
FROM 
    customer_data cd
ORDER BY 
    loyalty_score DESC, customer_id ASC;
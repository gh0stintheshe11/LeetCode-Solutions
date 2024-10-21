SELECT 
    curr.year AS year,
    curr.product_id,
    curr.curr_year_spend,
    prev.prev_year_spend,
    ROUND((curr.curr_year_spend - prev.prev_year_spend) / prev.prev_year_spend * 100, 2) AS yoy_rate
FROM (
    SELECT 
        YEAR(transaction_date) AS year,
        product_id, 
        SUM(spend) AS curr_year_spend
    FROM user_transactions
    GROUP BY product_id, year
) AS curr
LEFT JOIN (
    SELECT 
        YEAR(transaction_date) + 1 AS year,
        product_id, 
        SUM(spend) AS prev_year_spend
    FROM user_transactions
    GROUP BY product_id, year
) AS prev
ON curr.product_id = prev.product_id AND curr.year = prev.year
ORDER BY curr.product_id, curr.year
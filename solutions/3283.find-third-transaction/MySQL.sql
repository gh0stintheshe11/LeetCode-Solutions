SELECT user_id, spend AS third_transaction_spend, transaction_date AS third_transaction_date
FROM (
    SELECT 
        user_id, 
        spend, 
        transaction_date, 
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date) as rn,
        LAG(spend, 1) OVER (PARTITION BY user_id ORDER BY transaction_date) as prev_spend_1,
        LAG(spend, 2) OVER (PARTITION BY user_id ORDER BY transaction_date) as prev_spend_2
    FROM Transactions
) AS t
WHERE rn = 3 
    AND prev_spend_1 < spend 
    AND prev_spend_2 < spend
ORDER BY user_id;
SELECT t1.transaction_id
FROM Transactions t1
JOIN (
    SELECT DATE(day) AS day, MAX(amount) AS max_amount
    FROM Transactions
    GROUP BY DATE(day)
) t2 ON DATE(t1.day) = t2.day AND t1.amount = t2.max_amount
ORDER BY t1.transaction_id;
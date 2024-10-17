WITH CTE AS (
    SELECT 
        V.user_id, 
        V.visit_date, 
        COUNT(T.amount) AS transactions_count
    FROM 
        Visits V
    LEFT JOIN 
        Transactions T ON V.user_id = T.user_id AND V.visit_date = T.transaction_date
    GROUP BY 
        V.user_id, V.visit_date
),
TransactionCounts AS (
    SELECT DISTINCT transactions_count 
    FROM CTE
),
MaxCount AS (
    SELECT MAX(transactions_count) AS max_trans
    FROM TransactionCounts
),
AllCounts AS (
    SELECT n AS transactions_count
    FROM (
        SELECT @row := @row + 1 AS n
        FROM (SELECT 0 UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) t1,
             (SELECT 0 UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) t2,
             (SELECT @row := -1) AS init
    ) nums
    WHERE nums.n <= (SELECT max_trans FROM MaxCount)
)
SELECT 
    AC.transactions_count,
    COUNT(CASE WHEN CTE.transactions_count = AC.transactions_count THEN 1 END) AS visits_count
FROM 
    AllCounts AC
LEFT JOIN 
    CTE ON AC.transactions_count = CTE.transactions_count
GROUP BY 
    AC.transactions_count
ORDER BY 
    AC.transactions_count;
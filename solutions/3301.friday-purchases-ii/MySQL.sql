SELECT week_of_month, friday_date AS purchase_date, 
       COALESCE(SUM(P.amount_spend), 0) AS total_amount
FROM (
    SELECT 1 AS week_of_month, '2023-11-03' AS friday_date
    UNION ALL
    SELECT 2, '2023-11-10'
    UNION ALL
    SELECT 3, '2023-11-17'
    UNION ALL
    SELECT 4, '2023-11-24'
) AS Fridays
LEFT JOIN Purchases P ON Fridays.friday_date = P.purchase_date
GROUP BY week_of_month, friday_date
ORDER BY week_of_month;
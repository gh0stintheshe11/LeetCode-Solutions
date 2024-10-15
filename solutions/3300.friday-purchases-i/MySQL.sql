SELECT 
    CASE 
        WHEN WEEK(purchase_date, 3) = 44 THEN 1
        WHEN WEEK(purchase_date, 3) = 45 THEN 2
        WHEN WEEK(purchase_date, 3) = 46 THEN 3
        WHEN WEEK(purchase_date, 3) = 47 THEN 4
        ELSE 5
    END AS week_of_month,
    purchase_date,
    SUM(amount_spend) AS total_amount
FROM Purchases
WHERE DAYOFWEEK(purchase_date) = 6
GROUP BY week_of_month, purchase_date
ORDER BY week_of_month;
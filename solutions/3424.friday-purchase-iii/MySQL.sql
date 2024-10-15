WITH Fridays AS (
    SELECT DATE('2023-11-03') AS friday, 1 AS week_of_month
    UNION SELECT DATE('2023-11-10'), 2
    UNION SELECT DATE('2023-11-17'), 3
    UNION SELECT DATE('2023-11-24'), 4
),
PremiumVIPPurchases AS (
    SELECT P.purchase_date, U.membership, P.amount_spend
    FROM Purchases P
    JOIN Users U ON P.user_id = U.user_id
    WHERE U.membership IN ('Premium', 'VIP')
)
SELECT F.week_of_month, M.membership, IFNULL(SUM(A.amount_spend), 0) AS total_amount
FROM Fridays F
CROSS JOIN (SELECT DISTINCT membership FROM Users WHERE membership IN ('Premium', 'VIP')) M
LEFT JOIN PremiumVIPPurchases A ON F.friday = A.purchase_date AND M.membership = A.membership
GROUP BY F.week_of_month, M.membership
ORDER BY F.week_of_month, M.membership;
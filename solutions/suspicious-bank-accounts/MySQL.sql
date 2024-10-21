WITH MonthlyIncome AS (
    SELECT 
        account_id,
        EXTRACT(YEAR_MONTH FROM day) AS ym,
        SUM(amount) AS monthly_income
    FROM Transactions
    WHERE type = 'Creditor'
    GROUP BY account_id, EXTRACT(YEAR_MONTH FROM day)
),
FlaggedMonths AS (
    SELECT 
        m.account_id,
        m.ym,
        ROW_NUMBER() OVER (PARTITION BY m.account_id ORDER BY m.ym) as rn
    FROM MonthlyIncome m
    JOIN Accounts a ON m.account_id = a.account_id
    WHERE m.monthly_income > a.max_income
),
ConsecutiveFlagged AS (
    SELECT DISTINCT
        f1.account_id
    FROM FlaggedMonths f1
    JOIN FlaggedMonths f2 
    ON f1.account_id = f2.account_id AND f2.rn = f1.rn + 1 AND f2.ym = f1.ym + 1
)
SELECT account_id
FROM ConsecutiveFlagged;
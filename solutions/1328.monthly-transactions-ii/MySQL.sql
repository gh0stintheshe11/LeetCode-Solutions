WITH Approved AS (
    SELECT 
        DATE_FORMAT(trans_date, '%Y-%m') AS month,
        country,
        COUNT(*) AS approved_count,
        SUM(amount) AS approved_amount
    FROM 
        Transactions
    WHERE 
        state = 'approved'
    GROUP BY 
        month, country
),

ChargebackDetails AS (
    SELECT 
        DATE_FORMAT(c.trans_date, '%Y-%m') AS month,
        t.country,
        COUNT(c.trans_id) AS chargeback_count,
        SUM(t.amount) AS chargeback_amount
    FROM 
        Chargebacks c
    JOIN 
        Transactions t ON c.trans_id = t.id
    GROUP BY 
        month, t.country
)

SELECT 
    month,
    country,
    IFNULL(approved_count, 0) AS approved_count,
    IFNULL(approved_amount, 0) AS approved_amount,
    IFNULL(chargeback_count, 0) AS chargeback_count,
    IFNULL(chargeback_amount, 0) AS chargeback_amount
FROM (
    SELECT month, country FROM Approved
    UNION
    SELECT month, country FROM ChargebackDetails
) AS MonthsCountries
LEFT JOIN Approved USING(month, country)
LEFT JOIN ChargebackDetails USING(month, country)
WHERE 
    IFNULL(approved_count, 0) + IFNULL(chargeback_count, 0) > 0;
WITH p AS (
    SELECT s.account_id
    FROM Subscriptions s
    LEFT JOIN Streams t
    ON s.account_id = t.account_id
    GROUP BY s.account_id
    HAVING SUM(YEAR(start_date) = 2021 OR YEAR(end_date) = 2021) > 0 
           AND SUM(YEAR(stream_date) = 2021) = 0
)

SELECT COUNT(*) AS accounts_count
FROM p
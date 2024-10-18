WITH t0 AS (
    SELECT id, login_date, DATE_ADD(login_date, INTERVAL -DENSE_RANK() OVER(PARTITION BY id ORDER BY login_date) DAY) AS grp
    FROM (
        SELECT DISTINCT id, login_date
        FROM Logins
    ) l
)
SELECT DISTINCT t0.id, a.name
FROM t0
JOIN Accounts a ON t0.id = a.id
GROUP BY t0.id, t0.grp
HAVING DATEDIFF(MAX(login_date), MIN(login_date)) >= 4
ORDER BY t0.id;
# Write your MySQL query statement below
SELECT 
    activity_date AS login_date,
    COUNT(DISTINCT user_id) AS user_count
FROM 
    Traffic
WHERE 
    activity = 'login'
    AND activity_date BETWEEN '2019-04-01' AND '2019-06-30'
    AND activity_date = (
        SELECT MIN(activity_date)
        FROM Traffic t2
        WHERE t2.user_id = Traffic.user_id
          AND t2.activity = 'login'
    )
GROUP BY 
    activity_date
HAVING 
    user_count > 0
ORDER BY 
    login_date;
SELECT
    IFNULL(ROUND(COUNT(DISTINCT session_id)/(COUNT(DISTINCT user_id)*1.0), 2), 0.00) AS average_sessions_per_user
FROM
    (SELECT DISTINCT user_id, session_id
     FROM Activity
     WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27') AS active_sessions;
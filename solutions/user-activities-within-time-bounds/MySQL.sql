WITH cte AS (
    SELECT *,
            TIMESTAMPDIFF(
                hour,
                session_end,
                LEAD(session_start) OVER(PARTITION BY user_id, session_type ORDER BY session_start)) AS time_diff
    FROM Sessions
)

SELECT DISTINCT user_id
FROM cte
WHERE time_diff BETWEEN -12 AND 12
ORDER BY 1
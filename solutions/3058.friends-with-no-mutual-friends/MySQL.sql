WITH friend AS (
    SELECT user_id1, user_id2 FROM Friends
    UNION
    SELECT user_id2 AS user_id1, user_id1 AS user_id2 FROM Friends
),

forbidden AS (
    SELECT a.user_id1, b.user_id2 
    FROM friend a, friend b 
    WHERE a.user_id2 = b.user_id1
)

SELECT user_id1, user_id2 
FROM (
    SELECT a.user_id1, a.user_id2, b.user_id1 AS no
    FROM Friends a 
    LEFT JOIN forbidden b 
    ON a.user_id1 = b.user_id1 AND a.user_id2 = b.user_id2
) t
WHERE t.no IS NULL 
ORDER BY user_id1, user_id2
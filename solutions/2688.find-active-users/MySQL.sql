WITH data AS (
    SELECT *, ROW_NUMBER() OVER() AS i FROM Users
)
SELECT DISTINCT a.user_id 
FROM data a 
JOIN data b ON a.user_id = b.user_id AND a.i != b.i
WHERE ABS(DATEDIFF(a.created_at, b.created_at)) <= 7
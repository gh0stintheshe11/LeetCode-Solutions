WITH LeftMax AS (
    SELECT id, height, MAX(height) OVER (ORDER BY id) AS left_max
    FROM Heights
),
RightMax AS (
    SELECT id, height, MAX(height) OVER (ORDER BY id DESC) AS right_max
    FROM Heights
)
SELECT SUM(GREATEST(LEAST(l.left_max, r.right_max) - l.height, 0)) AS total_trapped_water
FROM LeftMax l
JOIN RightMax r ON l.id = r.id;
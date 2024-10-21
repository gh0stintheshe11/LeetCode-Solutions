WITH r_c AS (
    SELECT ROW_NUMBER() OVER (ORDER BY x, y) AS r, x, y
    FROM coordinates
)

SELECT DISTINCT x, y
FROM (
    SELECT CASE WHEN x1 < y1 THEN x1 ELSE x2 END AS x,
           CASE WHEN x1 < y1 THEN y1 ELSE y2 END AS y
    FROM (
        SELECT c1.x x1, c1.y y1, c2.x x2, c2.y y2
        FROM r_c c1
        JOIN r_c c2 ON c1.x = c2.y AND c1.y = c2.x AND c1.r != c2.r
    ) a
) a
ORDER BY x, y
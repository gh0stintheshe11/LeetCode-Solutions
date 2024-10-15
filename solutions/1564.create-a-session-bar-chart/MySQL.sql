SELECT '[0-5>' AS bin, 
       COUNT(CASE WHEN duration < 300 THEN 1 END) AS total
FROM Sessions
UNION ALL
SELECT '[5-10>' AS bin, 
       COUNT(CASE WHEN duration >= 300 AND duration < 600 THEN 1 END)
FROM Sessions
UNION ALL
SELECT '[10-15>' AS bin, 
       COUNT(CASE WHEN duration >= 600 AND duration < 900 THEN 1 END)
FROM Sessions
UNION ALL
SELECT '15 or more' AS bin, 
       COUNT(CASE WHEN duration >= 900 THEN 1 END)
FROM Sessions;
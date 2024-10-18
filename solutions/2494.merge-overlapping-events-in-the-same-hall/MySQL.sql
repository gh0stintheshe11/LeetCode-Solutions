SELECT 
       s1.start_day,
       MIN(t1.end_day) AS end_day,
       s1.hall_id
FROM HallEvents s1 
INNER JOIN HallEvents t1 ON s1.start_day <= t1.end_day AND s1.hall_id = t1.hall_id
  AND NOT EXISTS(SELECT * FROM HallEvents t2 
                 WHERE t1.end_day >= t2.start_day AND t1.end_day < t2.end_day AND s1.hall_id = t2.hall_id) 
WHERE NOT EXISTS(SELECT * FROM HallEvents s2 
                 WHERE s1.start_day > s2.start_day AND s1.start_day <= s2.end_day AND s1.hall_id = s2.hall_id) 
GROUP BY s1.start_day, s1.hall_id
ORDER BY s1.start_day, s1.hall_id
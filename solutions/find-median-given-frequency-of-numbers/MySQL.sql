SELECT ROUND(AVG(t1.num), 1) as median
FROM (
    SELECT num, frequency, 
           SUM(frequency) OVER (ORDER BY num) - frequency AS start_position
    FROM Numbers
) AS t1
JOIN (
    SELECT FLOOR((total_freq + 1) / 2) AS mid1, 
           FLOOR((total_freq + 2) / 2) AS mid2
    FROM (
        SELECT SUM(frequency) AS total_freq 
        FROM Numbers
    ) AS t
) AS t2
ON t2.mid1 BETWEEN t1.start_position + 1 AND t1.start_position + t1.frequency
   OR t2.mid2 BETWEEN t1.start_position + 1 AND t1.start_position + t1.frequency;
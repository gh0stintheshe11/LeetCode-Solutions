SELECT b.bus_id,
       COALESCE(SUM(CASE WHEN p.arrival_time <= b.arrival_time 
                      AND NOT EXISTS (
                          SELECT 1 
                          FROM Buses b2 
                          WHERE b2.arrival_time < b.arrival_time 
                          AND p.arrival_time <= b2.arrival_time
                      )
                   THEN 1 ELSE 0 END), 0) AS passengers_cnt
FROM Buses b
LEFT JOIN Passengers p ON p.arrival_time <= b.arrival_time
GROUP BY b.bus_id
ORDER BY b.bus_id;
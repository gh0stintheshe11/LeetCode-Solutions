SELECT 
    month_table.month AS month,
    ROUND(IFNULL(SUM(CASE WHEN ar.ride_id IS NOT NULL THEN ar.ride_distance ELSE 0 END) / 3, 0), 2) AS average_ride_distance,
    ROUND(IFNULL(SUM(CASE WHEN ar.ride_id IS NOT NULL THEN ar.ride_duration ELSE 0 END) / 3, 0), 2) AS average_ride_duration
FROM (
    SELECT 1 AS month UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 
    UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10
) AS month_table
LEFT JOIN Rides r 
    ON MONTH(r.requested_at) IN (month_table.month, month_table.month + 1, month_table.month + 2)
    AND YEAR(r.requested_at) = 2020
LEFT JOIN AcceptedRides ar 
    ON r.ride_id = ar.ride_id
GROUP BY month_table.month
ORDER BY month_table.month;
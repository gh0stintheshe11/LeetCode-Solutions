SELECT 
    m.month,
    (
        -- Calculate active drivers at the end of the month
        SELECT COUNT(DISTINCT driver_id)
        FROM Drivers
        WHERE join_date <= LAST_DAY(CONCAT('2020-', m.month, '-1'))
    ) AS active_drivers,
    (
        -- Calculate accepted rides in the month
        SELECT COUNT(DISTINCT ar.ride_id)
        FROM AcceptedRides ar
        JOIN Rides r ON ar.ride_id = r.ride_id
        WHERE MONTH(r.requested_at) = m.month AND YEAR(r.requested_at) = 2020
    ) AS accepted_rides
FROM 
    (SELECT 1 AS month UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 
     UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 
     UNION ALL SELECT 9 UNION ALL SELECT 10 UNION ALL SELECT 11 UNION ALL SELECT 12) m
ORDER BY 
    m.month;
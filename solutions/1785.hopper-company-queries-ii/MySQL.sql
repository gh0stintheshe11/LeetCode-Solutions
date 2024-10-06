WITH ActiveDrivers AS (
    SELECT 
        d.driver_id, 
        MONTH(d.join_date) AS join_month,
        YEAR(d.join_date) AS join_year
    FROM 
        Drivers d
    WHERE 
        YEAR(d.join_date) <= 2020
),
CumulativeActiveDrivers AS (
    SELECT 
        m.month,
        COUNT(DISTINCT ad.driver_id) AS active_drivers
    FROM 
        (SELECT 1 AS month UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION 
         SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10 UNION SELECT 11 UNION SELECT 12) m
    LEFT JOIN 
        ActiveDrivers ad ON (ad.join_year = 2019 AND m.month >= 1) OR (ad.join_year = 2020 AND m.month >= ad.join_month)
    WHERE 
        m.month <= 12
    GROUP BY 
        m.month
),
AcceptedRidesByMonth AS (
    SELECT 
        MONTH(r.requested_at) AS month,
        COUNT(DISTINCT ar.driver_id) AS working_drivers
    FROM 
        Rides r
    JOIN 
        AcceptedRides ar ON ar.ride_id = r.ride_id
    WHERE 
        YEAR(r.requested_at) = 2020
    GROUP BY 
        MONTH(r.requested_at)
)
SELECT 
    cad.month,
    CASE 
        WHEN cad.active_drivers = 0 THEN 0.00
        ELSE ROUND(COALESCE(arbm.working_drivers, 0) * 100.0 / cad.active_drivers, 2)
    END AS working_percentage
FROM 
    CumulativeActiveDrivers cad
LEFT JOIN 
    AcceptedRidesByMonth arbm ON cad.month = arbm.month
ORDER BY 
    cad.month;
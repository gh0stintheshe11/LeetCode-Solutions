WITH DriverTripStats AS (
    SELECT 
        v.fuel_type,
        v.driver_id,
        AVG(CAST(t.rating AS FLOAT)) AS avg_rating,
        SUM(t.distance) AS total_distance
    FROM Vehicles v
    JOIN Trips t ON v.vehicle_id = t.vehicle_id
    GROUP BY v.fuel_type, v.driver_id
),
DriverPerformance AS (
    SELECT 
        dts.fuel_type,
        dts.driver_id,
        ROUND(dts.avg_rating, 2) AS rating,
        dts.total_distance,
        d.accidents,
        ROW_NUMBER() OVER (
            PARTITION BY dts.fuel_type
            ORDER BY dts.avg_rating DESC, dts.total_distance DESC, d.accidents ASC
        ) AS rn
    FROM DriverTripStats dts
    JOIN Drivers d ON dts.driver_id = d.driver_id
)
SELECT
    dp.fuel_type,
    dp.driver_id,
    dp.rating,
    dp.total_distance AS distance
FROM DriverPerformance dp
WHERE dp.rn = 1
ORDER BY dp.fuel_type;
SELECT airport_id
FROM (
    SELECT departure_airport AS airport_id, SUM(flights_count) AS total_traffic
    FROM Flights
    GROUP BY departure_airport
    
    UNION ALL
    
    SELECT arrival_airport AS airport_id, SUM(flights_count) AS total_traffic
    FROM Flights
    GROUP BY arrival_airport
) AS combined_traffic
GROUP BY airport_id
HAVING SUM(total_traffic) = (
    SELECT MAX(total_traffic_sum)
    FROM (
        SELECT airport_id, SUM(total_traffic) AS total_traffic_sum
        FROM (
            SELECT departure_airport AS airport_id, flights_count AS total_traffic
            FROM Flights
            
            UNION ALL
            
            SELECT arrival_airport AS airport_id, flights_count AS total_traffic
            FROM Flights
        ) AS all_traffic
        GROUP BY airport_id
    ) AS total_traffic_sums
)
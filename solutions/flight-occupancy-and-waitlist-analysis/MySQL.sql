SELECT 
    f.flight_id,
    LEAST(COUNT(p.passenger_id), f.capacity) AS booked_cnt,
    GREATEST(COUNT(p.passenger_id) - f.capacity, 0) AS waitlist_cnt
FROM 
    Flights f
LEFT JOIN 
    Passengers p ON f.flight_id = p.flight_id
GROUP BY 
    f.flight_id
ORDER BY 
    f.flight_id;
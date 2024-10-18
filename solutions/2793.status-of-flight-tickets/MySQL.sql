SELECT p.passenger_id, 
       CASE 
           WHEN ROW_NUMBER() OVER (PARTITION BY p.flight_id ORDER BY p.booking_time) <= f.capacity THEN 'Confirmed' 
           ELSE 'Waitlist' 
       END AS Status
FROM Passengers p
JOIN Flights f ON p.flight_id = f.flight_id
ORDER BY p.passenger_id;
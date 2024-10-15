WITH HourlyCalls AS (
    SELECT city, HOUR(call_time) AS call_hour, COUNT(*) AS call_count
    FROM Calls
    GROUP BY city, HOUR(call_time)
),
MaxCallsPerCity AS (
    SELECT city, MAX(call_count) AS max_calls
    FROM HourlyCalls
    GROUP BY city
)
SELECT h.city, h.call_hour AS peak_calling_hour, h.call_count AS number_of_calls
FROM HourlyCalls h
JOIN MaxCallsPerCity m ON h.city = m.city AND h.call_count = m.max_calls
ORDER BY peak_calling_hour DESC, city DESC;
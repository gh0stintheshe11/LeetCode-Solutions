SELECT 
    c.country_name,
    CASE 
        WHEN AVG(weather_state) <= 15 THEN 'Cold'
        WHEN AVG(weather_state) >= 25 THEN 'Hot'
        ELSE 'Warm'
    END AS weather_type
FROM 
    Countries c
JOIN 
    Weather w ON c.country_id = w.country_id
WHERE 
    MONTH(w.day) = 11 AND YEAR(w.day) = 2019
GROUP BY 
    c.country_id
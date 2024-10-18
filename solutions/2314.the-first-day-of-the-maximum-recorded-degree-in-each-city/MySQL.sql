SELECT w.city_id, w.day, w.degree
FROM Weather w
JOIN (
    SELECT city_id, MAX(degree) as max_degree
    FROM Weather
    GROUP BY city_id
) md ON w.city_id = md.city_id AND w.degree = md.max_degree
WHERE w.day = (
    SELECT MIN(day)
    FROM Weather
    WHERE city_id = w.city_id AND degree = w.degree
)
ORDER BY w.city_id;
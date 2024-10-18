# Write your MySQL query statement below
WITH GlobalAverage AS (
    SELECT AVG(duration) AS avg_duration
    FROM Calls
),
CountryAverage AS (
    SELECT c.name AS country,
           AVG(cl.duration) AS avg_duration
    FROM Country c
    JOIN (
        SELECT p.id, SUBSTRING(p.phone_number, 1, 3) AS country_code
        FROM Person p
    ) p ON p.country_code = c.country_code
    JOIN Calls cl ON p.id IN (cl.caller_id, cl.callee_id)
    GROUP BY c.name
)
SELECT ca.country
FROM CountryAverage ca
JOIN GlobalAverage ga ON ca.avg_duration > ga.avg_duration;
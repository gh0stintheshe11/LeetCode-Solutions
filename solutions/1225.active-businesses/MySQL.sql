# Write your MySQL query statement below
SELECT DISTINCT business_id
FROM Events e1
JOIN (
    SELECT event_type, AVG(occurrences) AS avg_occurrences
    FROM Events
    GROUP BY event_type
) e2 ON e1.event_type = e2.event_type
WHERE e1.occurrences > e2.avg_occurrences
GROUP BY business_id
HAVING COUNT(DISTINCT e1.event_type) > 1;
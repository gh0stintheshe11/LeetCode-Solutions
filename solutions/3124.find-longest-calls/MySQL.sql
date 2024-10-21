WITH out_going AS
(
    SELECT contact_id, type, duration
    FROM Calls
    WHERE type = 'outgoing'
    ORDER BY duration DESC
    LIMIT 3
),
in_coming AS
(
    SELECT contact_id, type, duration
    FROM Calls
    WHERE type = 'incoming'
    ORDER BY duration DESC
    LIMIT 3
)

SELECT 
    first_name,
    type,
    TIME_FORMAT(SEC_TO_TIME(duration), '%H:%i:%s') AS duration_formatted
FROM Contacts c
JOIN
    (SELECT * FROM out_going
    UNION ALL
    SELECT * FROM in_coming) sub
ON c.id = sub.contact_id
ORDER BY 2 DESC, 3 DESC, 1 DESC
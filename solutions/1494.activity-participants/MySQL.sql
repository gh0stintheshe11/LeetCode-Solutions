SELECT activity
FROM (
    SELECT activity, COUNT(*) AS participant_count
    FROM Friends
    GROUP BY activity
) AS activity_participants
WHERE participant_count NOT IN (
    (SELECT MIN(participants) FROM (
        SELECT COUNT(*) AS participants
        FROM Friends
        GROUP BY activity
    ) AS counts),
    (SELECT MAX(participants) FROM (
        SELECT COUNT(*) AS participants
        FROM Friends
        GROUP BY activity
    ) AS counts)
);
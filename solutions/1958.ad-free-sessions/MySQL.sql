SELECT session_id
FROM Playback p
LEFT JOIN Ads a
ON p.customer_id = a.customer_id AND a.timestamp BETWEEN p.start_time AND p.end_time
WHERE a.ad_id IS NULL;
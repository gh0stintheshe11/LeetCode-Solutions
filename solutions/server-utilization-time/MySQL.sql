SELECT FLOOR(total_uptime_secs/3600/24)  AS total_uptime_days
FROM (
    SELECT  SUM(IF(session_status = 'stop', secs, 0)) - SUM(IF(session_status = 'start', secs, 0)) AS total_uptime_secs
    FROM (
        SELECT server_id, unix_timestamp(status_time) AS secs, session_status
        FROM Servers
    ) a 
) a
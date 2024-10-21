# Write your MySQL query statement below
WITH FirstSession AS (
    SELECT user_id, 
           MIN(session_start) AS first_session_start
    FROM Sessions
    GROUP BY user_id
),
FirstSessionType AS (
    SELECT s.user_id,
           f.first_session_start,
           s.session_type
    FROM FirstSession f
    JOIN Sessions s ON f.user_id = s.user_id AND f.first_session_start = s.session_start
),
ViewerFirst AS (
    SELECT user_id
    FROM FirstSessionType
    WHERE session_type = 'Viewer'
),
StreamerSessions AS (
    SELECT user_id, COUNT(*) AS sessions_count
    FROM Sessions
    WHERE session_type = 'Streamer'
    GROUP BY user_id
)
SELECT v.user_id, ss.sessions_count
FROM ViewerFirst v
JOIN StreamerSessions ss ON v.user_id = ss.user_id
ORDER BY ss.sessions_count DESC, v.user_id DESC;
# Write your MySQL query statement below
WITH install_dates AS (
    SELECT
        player_id,
        MIN(event_date) AS install_dt
    FROM
        Activity
    GROUP BY
        player_id
),
day1_logins AS (
    SELECT
        A.player_id,
        A.install_dt,
        IF(B.event_date = DATE_ADD(A.install_dt, INTERVAL 1 DAY), 1, 0) AS day1_login
    FROM
        install_dates A
    LEFT JOIN
        Activity B
    ON
        A.player_id = B.player_id
        AND B.event_date = DATE_ADD(A.install_dt, INTERVAL 1 DAY)
)
SELECT
    install_dt,
    COUNT(player_id) AS installs,
    ROUND(SUM(day1_login) / COUNT(player_id), 2) AS Day1_retention
FROM
    day1_logins
GROUP BY
    install_dt;
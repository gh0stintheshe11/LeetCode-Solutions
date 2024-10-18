WITH ReportedSpamPosts AS (
    SELECT DISTINCT action_date, post_id
    FROM Actions
    WHERE action = 'report' AND extra = 'spam'
),
RemovedSpamPosts AS (
    SELECT rsp.action_date, COUNT(DISTINCT rsp.post_id) AS removed
    FROM ReportedSpamPosts rsp
    JOIN Removals r ON rsp.post_id = r.post_id
    GROUP BY rsp.action_date
),
TotalSpamReports AS (
    SELECT action_date, COUNT(DISTINCT post_id) AS total_count
    FROM ReportedSpamPosts
    GROUP BY action_date
)

SELECT ROUND(AVG(IFNULL(rsp.removed / total_count.total_count, 0) * 100), 2) AS average_daily_percent
FROM TotalSpamReports total_count
LEFT JOIN RemovedSpamPosts rsp ON total_count.action_date = rsp.action_date;
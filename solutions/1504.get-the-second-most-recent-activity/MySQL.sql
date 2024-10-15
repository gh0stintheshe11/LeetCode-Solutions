SELECT username, activity, startDate, endDate
FROM (
    SELECT username, activity, startDate, endDate,
           ROW_NUMBER() OVER (PARTITION BY username ORDER BY endDate DESC) as rn,
           COUNT(*) OVER (PARTITION BY username) as cnt
    FROM UserActivity
) ranked
WHERE (rn = 2) OR (rn = 1 AND cnt = 1);
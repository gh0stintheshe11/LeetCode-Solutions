SELECT user_id, MAX(day_diff) AS biggest_window
FROM (
    SELECT user_id, 
           DATEDIFF(LEAD(visit_date, 1, '2021-01-01') OVER (PARTITION BY user_id ORDER BY visit_date), visit_date) AS day_diff
    FROM UserVisits
) AS calculated_diffs
GROUP BY user_id
ORDER BY user_id;
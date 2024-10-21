SELECT 
    a.age_bucket,
    ROUND(SUM(CASE WHEN act.activity_type = 'send' THEN act.time_spent ELSE 0 END) / SUM(act.time_spent) * 100, 2) AS send_perc,
    ROUND(SUM(CASE WHEN act.activity_type = 'open' THEN act.time_spent ELSE 0 END) / SUM(act.time_spent) * 100, 2) AS open_perc
FROM 
    Activities act
JOIN 
    Age a ON act.user_id = a.user_id
GROUP BY 
    a.age_bucket;
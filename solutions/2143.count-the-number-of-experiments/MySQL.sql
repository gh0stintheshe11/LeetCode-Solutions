SELECT 
    p.platform, 
    e.experiment_name, 
    COUNT(ex.experiment_id) AS num_experiments
FROM 
    (SELECT 'Android' AS platform
     UNION ALL
     SELECT 'IOS'
     UNION ALL
     SELECT 'Web') p
CROSS JOIN 
    (SELECT 'Reading' AS experiment_name
     UNION ALL
     SELECT 'Sports'
     UNION ALL
     SELECT 'Programming') e
LEFT JOIN 
    Experiments ex
ON 
    ex.platform = p.platform AND ex.experiment_name = e.experiment_name
GROUP BY 
    p.platform, e.experiment_name;
SELECT 
    t.task_id, 
    n.n AS subtask_id
FROM 
    Tasks t
JOIN 
    (
        SELECT 1 AS n UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 
        UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 
        UNION SELECT 9 UNION SELECT 10 UNION SELECT 11 UNION SELECT 12 
        UNION SELECT 13 UNION SELECT 14 UNION SELECT 15 UNION SELECT 16 
        UNION SELECT 17 UNION SELECT 18 UNION SELECT 19 UNION SELECT 20
    ) n
ON 
    n.n <= t.subtasks_count
LEFT JOIN 
    Executed e
ON 
    t.task_id = e.task_id 
    AND n.n = e.subtask_id
WHERE 
    e.subtask_id IS NULL
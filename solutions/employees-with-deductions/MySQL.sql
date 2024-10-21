SELECT e.employee_id
FROM Employees e
LEFT JOIN (
    SELECT l.employee_id, 
           SUM(TIMESTAMPDIFF(MINUTE, l.in_time, l.out_time) + 
               IF(SECOND(l.out_time) > 0 OR SECOND(l.in_time) > 0, 1, 0)) / 60 AS worked_hours
    FROM Logs l
    GROUP BY l.employee_id
) worked ON e.employee_id = worked.employee_id
WHERE worked.worked_hours IS NULL OR worked.worked_hours < e.needed_hours;
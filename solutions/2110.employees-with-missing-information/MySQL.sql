SELECT t1.employee_id
FROM (
    SELECT employee_id FROM Employees 
    UNION 
    SELECT employee_id FROM Salaries
) AS t1
LEFT JOIN Employees e ON t1.employee_id = e.employee_id
LEFT JOIN Salaries s ON t1.employee_id = s.employee_id
WHERE e.name IS NULL OR s.salary IS NULL
ORDER BY t1.employee_id;
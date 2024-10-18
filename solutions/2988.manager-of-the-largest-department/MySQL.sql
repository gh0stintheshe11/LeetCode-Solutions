SELECT e.emp_name AS manager_name, e.dep_id
FROM Employees e
JOIN (
    SELECT dep_id, COUNT(*) AS employee_count
    FROM Employees
    GROUP BY dep_id
) d ON e.dep_id = d.dep_id
JOIN (
    SELECT dep_id, MAX(employee_count) AS max_count
    FROM (
        SELECT dep_id, COUNT(*) AS employee_count
        FROM Employees
        GROUP BY dep_id
    ) AS counts
) max_d ON d.employee_count = max_d.max_count
WHERE e.position = 'Manager'
ORDER BY e.dep_id;
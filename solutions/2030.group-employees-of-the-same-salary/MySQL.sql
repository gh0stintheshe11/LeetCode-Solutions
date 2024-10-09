SELECT e.employee_id, e.name, e.salary, t.team_id
FROM Employees e
JOIN (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary) as team_id
    FROM Employees
    GROUP BY salary
    HAVING COUNT(*) > 1
) t ON e.salary = t.salary
ORDER BY t.team_id, e.employee_id;
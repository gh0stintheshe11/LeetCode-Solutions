WITH RECURSIVE ReportToHead AS (
    SELECT employee_id
    FROM Employees
    WHERE manager_id = 1 AND employee_id != 1
    UNION
    SELECT e.employee_id
    FROM Employees e
    INNER JOIN ReportToHead rth ON e.manager_id = rth.employee_id
)
SELECT employee_id
FROM ReportToHead;
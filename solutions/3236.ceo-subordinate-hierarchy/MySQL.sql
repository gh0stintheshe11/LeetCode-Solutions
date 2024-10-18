WITH RECURSIVE Hierarchy AS (
    SELECT 
        e.employee_id AS subordinate_id,
        e.employee_name AS subordinate_name,
        1 AS hierarchy_level,
        e.salary - c.salary AS salary_difference
    FROM
        Employees e
    JOIN 
        (SELECT employee_id, salary 
         FROM Employees 
         WHERE manager_id IS NULL) c
    ON 
        e.manager_id = c.employee_id
    UNION ALL
    SELECT 
        e.employee_id AS subordinate_id,
        e.employee_name AS subordinate_name,
        h.hierarchy_level + 1 AS hierarchy_level,
        e.salary - ceo.salary AS salary_difference
    FROM 
        Employees e
    JOIN 
        Hierarchy h
    ON 
        e.manager_id = h.subordinate_id
    JOIN
        (SELECT employee_id, salary 
         FROM Employees 
         WHERE manager_id IS NULL) ceo
    ON 
        1=1
)

SELECT 
    subordinate_id,
    subordinate_name,
    hierarchy_level,
    salary_difference
FROM 
    Hierarchy
ORDER BY 
    hierarchy_level ASC, subordinate_id ASC;
SELECT 
    s.company_id, 
    s.employee_id, 
    s.employee_name, 
    ROUND(s.salary * 
      (1 - 
        CASE 
          WHEN t.max_salary < 1000 THEN 0
          WHEN t.max_salary BETWEEN 1000 AND 10000 THEN 0.24
          ELSE 0.49
        END)) AS salary
FROM 
    Salaries s
JOIN 
    (SELECT 
        company_id, 
        MAX(salary) AS max_salary 
     FROM 
        Salaries 
     GROUP BY 
        company_id) t
ON 
    s.company_id = t.company_id;
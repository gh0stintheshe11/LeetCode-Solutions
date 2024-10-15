# Write your MySQL query statement below

SELECT emp_id, firstname, lastname, salary, department_id
FROM Salary
WHERE (emp_id, salary) IN (
    SELECT emp_id, MAX(salary) as max_salary
    FROM Salary
    GROUP BY emp_id
)
ORDER BY emp_id;
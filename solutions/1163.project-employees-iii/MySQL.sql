# Write your MySQL query statement below
SELECT p.project_id, p.employee_id
FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
WHERE (p.project_id, e.experience_years) IN (
    SELECT project_id, MAX(experience_years)
    FROM Project
    JOIN Employee ON Project.employee_id = Employee.employee_id
    GROUP BY project_id
);
SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee
JOIN (
    SELECT departmentId, MAX(salary) AS max_salary
    FROM Employee
    GROUP BY departmentId
) AS MaxSalary
ON Employee.departmentId = MaxSalary.departmentId 
AND Employee.salary = MaxSalary.max_salary
JOIN Department
ON Employee.departmentId = Department.id
WITH DistinctSalaries AS (
    SELECT DISTINCT e.departmentId, e.salary
    FROM Employee e
),
RankedSalaries AS (
    SELECT 
        departmentId,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS SalaryRank
    FROM 
        DistinctSalaries
)
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM 
    RankedSalaries rs
JOIN 
    Employee e ON rs.departmentId = e.departmentId AND rs.salary = e.salary
JOIN 
    Department d ON rs.departmentId = d.id
WHERE 
    rs.SalaryRank <= 3
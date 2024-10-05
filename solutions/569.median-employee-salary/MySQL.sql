# Write your MySQL query statement below

SELECT id, company, salary
FROM (
    SELECT id, company, salary, 
           ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary, id) AS row_num,
           COUNT(*) OVER (PARTITION BY company) AS total_count
    FROM Employee
) ranked_employees
WHERE (total_count % 2 = 1 AND row_num = (total_count + 1) / 2) OR
      (total_count % 2 = 0 AND (row_num = total_count / 2 OR row_num = total_count / 2 + 1))
ORDER BY company, salary, id;
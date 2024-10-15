# Write your MySQL query statement below

SELECT 
    d.dept_name,
    COUNT(s.student_id) AS student_number
FROM 
    Department d
LEFT JOIN 
    Student s
ON 
    d.dept_id = s.dept_id
GROUP BY 
    d.dept_id
ORDER BY 
    student_number DESC,
    d.dept_name;
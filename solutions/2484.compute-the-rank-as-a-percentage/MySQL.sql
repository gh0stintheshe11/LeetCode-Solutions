WITH rank_students AS (
    SELECT 
        department_id, 
        student_id, 
        mark, 
        RANK() OVER (PARTITION BY department_id ORDER BY mark DESC) AS rank_student
    FROM Students
),
count_students_dept AS (
    SELECT 
        department_id, 
        COUNT(student_id) AS count_dept 
    FROM Students 
    GROUP BY department_id
)
SELECT 
    r.student_id, 
    r.department_id, 
    ROUND(COALESCE((r.rank_student-1)*100/(c.count_dept-1),0), 2) AS percentage
FROM 
    rank_students AS r
LEFT JOIN 
    count_students_dept AS c
ON 
    r.department_id = c.department_id
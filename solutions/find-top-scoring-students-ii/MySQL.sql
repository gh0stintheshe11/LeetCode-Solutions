SELECT 
    e.student_id
FROM 
    enrollments e
JOIN 
    courses c ON c.course_id = e.course_id 
JOIN 
    students s ON s.student_id = e.student_id
GROUP BY 
    e.student_id, s.major
HAVING 
    SUM(CASE WHEN c.major = s.major AND c.mandatory = 'Yes' AND e.grade = 'A' THEN 1 ELSE 0 END) = 
    (SELECT COUNT(DISTINCT course_id) FROM courses WHERE major = s.major AND mandatory = 'Yes' GROUP BY major)
    AND 
    SUM(CASE WHEN c.major = s.major AND c.mandatory = 'No' AND e.grade IN ('A', 'B') THEN 1 ELSE 0 END) > 1
    AND 
    AVG(e.gpa) >= 2.5
ORDER BY 
    e.student_id;
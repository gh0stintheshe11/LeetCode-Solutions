SELECT 
    s.student_id
FROM courses c
JOIN students s
    ON c.major = s.major
LEFT JOIN enrollments e
    ON s.student_id = e.student_id
    AND c.course_id = e.course_id
GROUP BY student_id
HAVING SUM(CASE WHEN grade='A' THEN 0 ELSE 1 END) = 0  
ORDER BY student_id
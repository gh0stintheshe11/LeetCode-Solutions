SELECT e.student_id, e.course_id, e.grade
FROM Enrollments e
JOIN (
    SELECT student_id, MAX(grade) AS max_grade
    FROM Enrollments
    GROUP BY student_id
) AS max_grades ON e.student_id = max_grades.student_id AND e.grade = max_grades.max_grade
JOIN (
    SELECT student_id, grade, MIN(course_id) AS min_course_id
    FROM Enrollments
    GROUP BY student_id, grade
) AS min_courses ON e.student_id = min_courses.student_id 
                 AND e.grade = min_courses.grade 
                 AND e.course_id = min_courses.min_course_id
ORDER BY e.student_id;
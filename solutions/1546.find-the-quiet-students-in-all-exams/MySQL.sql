SELECT S.student_id, S.student_name
FROM Student S
WHERE NOT EXISTS (
    SELECT 1
    FROM Exam E
    WHERE E.student_id = S.student_id
    AND (E.score = (SELECT MAX(score) FROM Exam WHERE exam_id = E.exam_id)
         OR E.score = (SELECT MIN(score) FROM Exam WHERE exam_id = E.exam_id))
)
AND EXISTS (
    SELECT 1
    FROM Exam E2
    WHERE E2.student_id = S.student_id
)
ORDER BY S.student_id;
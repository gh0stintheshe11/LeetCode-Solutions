SELECT 
    s.school_id,
    COALESCE(
        (
            SELECT MIN(e.score)
            FROM Exam e
            WHERE e.student_count <= s.capacity
        ), 
        -1
    ) AS score
FROM 
    Schools s;
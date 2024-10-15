SELECT 
    MAX(total_score) - MIN(total_score) AS difference_in_score
FROM (
    SELECT 
        student_id,
        (assignment1 + assignment2 + assignment3) AS total_score
    FROM Scores
) AS subquery;
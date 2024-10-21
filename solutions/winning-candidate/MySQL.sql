# Write your MySQL query statement below
SELECT name
FROM Candidate
WHERE id = (
    SELECT candidateId
    FROM Vote
    GROUP BY candidateId
    ORDER BY COUNT(*) DESC
    LIMIT 1
);
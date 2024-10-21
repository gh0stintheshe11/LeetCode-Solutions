SELECT candidate
FROM (
    SELECT candidate, SUM(1.0 / count_per_voter) AS total_votes
    FROM (
        SELECT voter, candidate, COUNT(candidate) OVER (PARTITION BY voter) AS count_per_voter
        FROM Votes
        WHERE candidate IS NOT NULL
    ) AS subquery
    GROUP BY candidate
) AS total_votes_per_candidate
WHERE total_votes = (
    SELECT MAX(total_votes)
    FROM (
        SELECT candidate, SUM(1.0 / count_per_voter) AS total_votes
        FROM (
            SELECT voter, candidate, COUNT(candidate) OVER (PARTITION BY voter) AS count_per_voter
            FROM Votes
            WHERE candidate IS NOT NULL
        ) AS subquery_inner
        GROUP BY candidate
    ) AS total_votes_per_candidate_inner
)
ORDER BY candidate;
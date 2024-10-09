WITH MedalWinners AS (
    SELECT user_id, contest_id FROM (
        SELECT contest_id, gold_medal AS user_id FROM Contests
        UNION ALL
        SELECT contest_id, silver_medal FROM Contests
        UNION ALL
        SELECT contest_id, bronze_medal FROM Contests
    ) AS AllMedals
),
ConsecutiveMedals AS (
    SELECT user_id, COUNT(DISTINCT contest_id) AS cnt
    FROM (
        SELECT user_id, contest_id,
               contest_id - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY contest_id) AS grp
        FROM MedalWinners
    ) AS GrpTable
    GROUP BY user_id, grp
    HAVING cnt >= 3
),
GoldMedals AS (
    SELECT gold_medal AS user_id, COUNT(DISTINCT contest_id) AS cnt
    FROM Contests
    GROUP BY gold_medal
    HAVING cnt >= 3
),
InterviewCandidates AS (
    SELECT DISTINCT user_id FROM ConsecutiveMedals
    UNION
    SELECT DISTINCT user_id FROM GoldMedals
)
SELECT u.name, u.mail
FROM InterviewCandidates ic
JOIN Users u ON ic.user_id = u.user_id;
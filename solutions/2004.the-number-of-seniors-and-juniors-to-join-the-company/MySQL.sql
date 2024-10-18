WITH SeniorHiring AS (
    SELECT 
        experience, 
        salary,
        SUM(salary) OVER (PARTITION BY experience ORDER BY salary) AS cumulative_salary,
        ROW_NUMBER() OVER (PARTITION BY experience ORDER BY salary) AS rn
    FROM Candidates
    WHERE experience = 'Senior'
),
JuniorHiring AS (
    SELECT 
        experience, 
        salary,
        SUM(salary) OVER (PARTITION BY experience ORDER BY salary) AS cumulative_salary,
        ROW_NUMBER() OVER (PARTITION BY experience ORDER BY salary) AS rn
    FROM Candidates
    WHERE experience = 'Junior'
)

SELECT 'Senior' AS experience, COALESCE(MAX(rn), 0) AS accepted_candidates
FROM SeniorHiring
WHERE cumulative_salary <= 70000

UNION ALL

SELECT 'Junior' AS experience, COALESCE(MAX(rn), 0) AS accepted_candidates
FROM JuniorHiring
WHERE cumulative_salary <= 70000 - (
   SELECT COALESCE(MAX(cumulative_salary), 0) 
   FROM SeniorHiring
   WHERE cumulative_salary <= 70000
);
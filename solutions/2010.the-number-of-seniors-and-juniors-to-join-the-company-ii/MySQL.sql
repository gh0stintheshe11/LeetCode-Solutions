WITH SeniorHires AS (
    SELECT employee_id, salary
    FROM Candidates
    WHERE experience = 'Senior'
    ORDER BY salary
),
JuniorHires AS (
    SELECT employee_id, salary
    FROM Candidates
    WHERE experience = 'Junior'
    ORDER BY salary
),
HiredSeniors AS (
    SELECT employee_id, salary, SUM(salary) OVER (ORDER BY salary) AS cumulative_salary
    FROM SeniorHires
),
SelectedSeniors AS (
    SELECT employee_id
    FROM HiredSeniors
    WHERE cumulative_salary <= 70000
),
RemainingBudget AS (
    SELECT 70000 - COALESCE(MAX(cumulative_salary), 0) AS budget
    FROM HiredSeniors 
    WHERE cumulative_salary <= 70000
),
HiredJuniors AS (
    SELECT j.employee_id, j.salary, SUM(j.salary) OVER (ORDER BY j.salary) AS cumulative_salary
    FROM JuniorHires j, RemainingBudget r
    WHERE j.salary <= r.budget
)
SELECT employee_id
FROM SelectedSeniors
UNION ALL
SELECT employee_id
FROM HiredJuniors
WHERE cumulative_salary <= (SELECT budget FROM RemainingBudget);
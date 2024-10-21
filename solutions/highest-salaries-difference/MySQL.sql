SELECT
    ABS(
        (SELECT MAX(salary) FROM Salaries WHERE department = 'Engineering') -
        (SELECT MAX(salary) FROM Salaries WHERE department = 'Marketing')
    ) AS salary_difference
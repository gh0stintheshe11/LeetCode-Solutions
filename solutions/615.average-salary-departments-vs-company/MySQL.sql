WITH MonthlyCompanyAvg AS (
    SELECT
        DATE_FORMAT(pay_date, '%Y-%m') AS pay_month,
        AVG(amount) AS company_avg
    FROM Salary
    GROUP BY DATE_FORMAT(pay_date, '%Y-%m')
),
MonthlyDepartmentAvg AS (
    SELECT
        DATE_FORMAT(S.pay_date, '%Y-%m') AS pay_month,
        E.department_id,
        AVG(S.amount) AS department_avg
    FROM Salary S
    JOIN Employee E
    ON S.employee_id = E.employee_id
    GROUP BY DATE_FORMAT(S.pay_date, '%Y-%m'), E.department_id
)
SELECT
    MDA.pay_month,
    MDA.department_id,
    CASE
        WHEN MDA.department_avg > MCA.company_avg THEN 'higher'
        WHEN MDA.department_avg < MCA.company_avg THEN 'lower'
        ELSE 'same'
    END AS comparison
FROM MonthlyDepartmentAvg MDA
JOIN MonthlyCompanyAvg MCA
ON MDA.pay_month = MCA.pay_month;
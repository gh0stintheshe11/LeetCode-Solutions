WITH Dates AS (
    SELECT fail_date AS date, 'failed' AS status FROM Failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
    UNION
    SELECT success_date, 'succeeded' FROM Succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
),
OrderedDates AS (
    SELECT date, status,
           ROW_NUMBER() OVER (ORDER BY date) AS row_num,
           ROW_NUMBER() OVER (PARTITION BY status ORDER BY date) AS status_row_num
    FROM Dates
),
GroupedDates AS (
    SELECT date, status,
           row_num - status_row_num AS grp
    FROM OrderedDates
)
SELECT status AS period_state,
       MIN(date) AS start_date,
       MAX(date) AS end_date
FROM GroupedDates
GROUP BY status, grp
ORDER BY start_date;
SELECT
    SUM(CASE WHEN DAYOFWEEK(submit_date) IN (1, 7) THEN 1 ELSE 0 END) AS weekend_cnt,
    SUM(CASE WHEN DAYOFWEEK(submit_date) BETWEEN 2 AND 6 THEN 1 ELSE 0 END) AS working_cnt
FROM
    Tasks;
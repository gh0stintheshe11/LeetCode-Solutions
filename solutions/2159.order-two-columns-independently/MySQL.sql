WITH row_number_first AS (
    SELECT first_col, 
       ROW_NUMBER() OVER (ORDER BY first_col) AS row_num
    FROM Data
    ),
    row_number_second AS (
    SELECT second_col, 
       ROW_NUMBER() OVER (ORDER BY second_col DESC) AS row_num
    FROM Data
    )
SELECT t1.first_col,
       t2.second_col
FROM row_number_first t1 
JOIN row_number_second t2 
ON  t1.row_num = t2.row_num;
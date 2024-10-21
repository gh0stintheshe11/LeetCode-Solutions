SELECT 
    CONCAT(
        GROUP_CONCAT(
            CONCAT(
                IF(factor >= 0, '+', ''),
                factor,
                CASE 
                    WHEN power = 0 THEN ''
                    WHEN power = 1 THEN 'X'
                    ELSE CONCAT('X^', power)
                END
            ) ORDER BY power DESC
            SEPARATOR ''
        ),
        '=0'
    ) AS equation
FROM Terms;
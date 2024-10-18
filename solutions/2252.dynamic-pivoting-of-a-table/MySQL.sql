CREATE PROCEDURE PivotProducts()
BEGIN
    SET SESSION group_concat_max_len = 10000;

    SET @sql = NULL;

    SELECT
        GROUP_CONCAT(
            DISTINCT
            CONCAT(
                'MAX(CASE WHEN store = ''',
                store,
                ''' THEN price END) AS `',
                store,
                '`'
            )
            ORDER BY store
        ) INTO @sql
    FROM Products;

    SET @sql = CONCAT('SELECT product_id, ', @sql, ' FROM Products GROUP BY product_id');

    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END
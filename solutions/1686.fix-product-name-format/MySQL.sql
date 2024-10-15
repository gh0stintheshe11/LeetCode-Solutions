SELECT 
    LOWER(TRIM(product_name)) AS product_name,
    DATE_FORMAT(sale_date, '%Y-%m') AS sale_date,
    COUNT(*) AS total
FROM 
    Sales
GROUP BY 
    LOWER(TRIM(product_name)),
    DATE_FORMAT(sale_date, '%Y-%m')
ORDER BY 
    product_name ASC, 
    sale_date ASC;
SELECT p.product_id, p.product_name
FROM Product p
JOIN Sales s ON p.product_id = s.product_id
WHERE s.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY p.product_id, p.product_name
HAVING COUNT(*) = (
    SELECT COUNT(*)
    FROM Sales s2
    WHERE s2.product_id = p.product_id
)
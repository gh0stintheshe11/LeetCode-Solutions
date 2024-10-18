SELECT p.product_id, p.quantity, p.quantity * pr.price AS price
FROM Purchases p
JOIN Products pr ON p.product_id = pr.product_id
WHERE p.invoice_id = (
    SELECT p1.invoice_id
    FROM Purchases p1
    JOIN Products pr1 ON p1.product_id = pr1.product_id
    GROUP BY p1.invoice_id
    ORDER BY SUM(p1.quantity * pr1.price) DESC, p1.invoice_id
    LIMIT 1
);
SELECT c.customer_id, c.name
FROM Customers c
WHERE c.customer_id IN (
    SELECT o1.customer_id
    FROM Orders o1
    JOIN Product p1 ON o1.product_id = p1.product_id
    WHERE MONTH(o1.order_date) = 6 AND YEAR(o1.order_date) = 2020
    GROUP BY o1.customer_id
    HAVING SUM(p1.price * o1.quantity) >= 100
)
AND c.customer_id IN (
    SELECT o2.customer_id
    FROM Orders o2
    JOIN Product p2 ON o2.product_id = p2.product_id
    WHERE MONTH(o2.order_date) = 7 AND YEAR(o2.order_date) = 2020
    GROUP BY o2.customer_id
    HAVING SUM(p2.price * o2.quantity) >= 100
)
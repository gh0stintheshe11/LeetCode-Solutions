SELECT name AS customer_name, o.customer_id, order_id, order_date
FROM (
    SELECT order_id, order_date, customer_id,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS order_rank
    FROM Orders
) o
JOIN Customers c ON o.customer_id = c.customer_id
WHERE o.order_rank <= 3
ORDER BY c.name, o.customer_id, o.order_date DESC;
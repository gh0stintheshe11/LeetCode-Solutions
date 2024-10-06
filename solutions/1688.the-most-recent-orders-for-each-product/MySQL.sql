SELECT 
    p.product_name, 
    o.product_id, 
    o.order_id, 
    o.order_date
FROM 
    Orders o
JOIN 
    (SELECT product_id, MAX(order_date) AS max_order_date
     FROM Orders
     GROUP BY product_id) recent_orders
ON 
    o.product_id = recent_orders.product_id AND 
    o.order_date = recent_orders.max_order_date
JOIN 
    Products p
ON 
    o.product_id = p.product_id
ORDER BY 
    p.product_name ASC, 
    o.product_id ASC, 
    o.order_id ASC;
SELECT DISTINCT o1.product_id
FROM 
    (SELECT product_id, YEAR(purchase_date) AS order_year, COUNT(DISTINCT order_id) AS order_count
     FROM Orders 
     GROUP BY product_id, YEAR(purchase_date)) o1
JOIN 
    (SELECT product_id, YEAR(purchase_date) AS order_year, COUNT(DISTINCT order_id) AS order_count
     FROM Orders 
     GROUP BY product_id, YEAR(purchase_date)) o2
ON o1.product_id = o2.product_id 
   AND o1.order_year = o2.order_year - 1
WHERE o1.order_count >= 3 AND o2.order_count >= 3;
SELECT 
    order_date,
    ROUND(SUM(customer_pref_delivery_date = order_date) / COUNT(delivery_id) * 100, 2) AS immediate_percentage
FROM 
    Delivery
GROUP BY 
    order_date
ORDER BY 
    order_date;
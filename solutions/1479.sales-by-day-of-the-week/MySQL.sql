SELECT 
    I.item_category AS Category,
    COALESCE(SUM(CASE WHEN DAYNAME(O.order_date) = 'Monday' THEN O.quantity ELSE 0 END), 0) AS Monday,
    COALESCE(SUM(CASE WHEN DAYNAME(O.order_date) = 'Tuesday' THEN O.quantity ELSE 0 END), 0) AS Tuesday,
    COALESCE(SUM(CASE WHEN DAYNAME(O.order_date) = 'Wednesday' THEN O.quantity ELSE 0 END), 0) AS Wednesday,
    COALESCE(SUM(CASE WHEN DAYNAME(O.order_date) = 'Thursday' THEN O.quantity ELSE 0 END), 0) AS Thursday,
    COALESCE(SUM(CASE WHEN DAYNAME(O.order_date) = 'Friday' THEN O.quantity ELSE 0 END), 0) AS Friday,
    COALESCE(SUM(CASE WHEN DAYNAME(O.order_date) = 'Saturday' THEN O.quantity ELSE 0 END), 0) AS Saturday,
    COALESCE(SUM(CASE WHEN DAYNAME(O.order_date) = 'Sunday' THEN O.quantity ELSE 0 END), 0) AS Sunday
FROM 
    Items I
LEFT JOIN 
    Orders O
ON 
    I.item_id = O.item_id
GROUP BY 
    I.item_category
ORDER BY 
    I.item_category;
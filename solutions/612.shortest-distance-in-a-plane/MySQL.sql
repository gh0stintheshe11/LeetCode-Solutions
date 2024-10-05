SELECT 
    ROUND(
        SQRT(
            POWER(p1.x - p2.x, 2) + 
            POWER(p1.y - p2.y, 2)
        ), 2
    ) AS shortest
FROM 
    Point2D p1
JOIN 
    Point2D p2 
ON 
    p1.x != p2.x OR p1.y != p2.y
ORDER BY 
    shortest
LIMIT 1;
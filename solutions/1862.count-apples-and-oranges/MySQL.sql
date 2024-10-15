# Write your MySQL query statement below
SELECT 
    SUM(b.apple_count + IFNULL(c.apple_count, 0)) AS apple_count, 
    SUM(b.orange_count + IFNULL(c.orange_count, 0)) AS orange_count
FROM 
    Boxes b
LEFT JOIN 
    Chests c ON b.chest_id = c.chest_id;
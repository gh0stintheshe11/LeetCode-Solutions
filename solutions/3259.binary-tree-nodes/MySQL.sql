# Write your MySQL query statement below
SELECT 
    N, 
    CASE 
        WHEN P IS NULL THEN 'Root'
        WHEN N NOT IN (SELECT DISTINCT P FROM Tree WHERE P IS NOT NULL) THEN 'Leaf'
        ELSE 'Inner'
    END AS Type
FROM 
    Tree
ORDER BY 
    N ASC;
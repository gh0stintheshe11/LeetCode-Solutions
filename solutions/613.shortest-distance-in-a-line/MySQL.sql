# Write your MySQL query statement below
SELECT MIN(ABS(p2.x - p1.x)) AS shortest
FROM Point p1, Point p2
WHERE p1.x != p2.x;
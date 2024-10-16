SELECT email 
FROM Person
GROUP BY email
HAVING COUNT(id) > 1;
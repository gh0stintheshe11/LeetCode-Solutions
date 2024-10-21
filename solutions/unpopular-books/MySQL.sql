# Write your MySQL query statement below
SELECT b.book_id, b.name
FROM Books b
LEFT JOIN (
    SELECT o.book_id, SUM(o.quantity) AS total_quantity
    FROM Orders o
    WHERE o.dispatch_date >= '2018-06-23' AND o.dispatch_date < '2019-06-23'
    GROUP BY o.book_id
) sales ON b.book_id = sales.book_id
WHERE (sales.total_quantity < 10 OR sales.total_quantity IS NULL)
AND b.available_from <= '2019-05-23';
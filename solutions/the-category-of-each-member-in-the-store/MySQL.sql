SELECT m.member_id, m.name,
       CASE 
           WHEN v.visit_count IS NULL THEN 'Bronze'
           WHEN v.purchase_count * 100 / v.visit_count >= 80 THEN 'Diamond'
           WHEN v.purchase_count * 100 / v.visit_count >= 50 THEN 'Gold'
           ELSE 'Silver'
       END AS category
FROM Members m
LEFT JOIN (
    SELECT v.member_id,
           COUNT(DISTINCT v.visit_id) AS visit_count,
           COUNT(DISTINCT p.visit_id) AS purchase_count
    FROM Visits v
    LEFT JOIN Purchases p ON v.visit_id = p.visit_id
    GROUP BY v.member_id
) v ON m.member_id = v.member_id;
SELECT U.user_id AS seller_id,
       CASE
           WHEN O2.item_brand = U.favorite_brand THEN 'yes'
           ELSE 'no'
       END AS 2nd_item_fav_brand
FROM Users U
LEFT JOIN (
    SELECT O.seller_id, I.item_brand, 
           ROW_NUMBER() OVER (PARTITION BY O.seller_id ORDER BY O.order_date) rn
    FROM Orders O
    JOIN Items I ON O.item_id = I.item_id
) O2 ON U.user_id = O2.seller_id AND O2.rn = 2;
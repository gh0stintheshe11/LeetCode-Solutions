WITH SellerNonFavItems AS (
    SELECT O.seller_id, I.item_id
    FROM Orders O
    JOIN Users U ON O.seller_id = U.seller_id
    JOIN Items I ON O.item_id = I.item_id
    WHERE I.item_brand <> U.favorite_brand
    GROUP BY O.seller_id, I.item_id
),
SellerUniqueItemCounts AS (
    SELECT seller_id, COUNT(DISTINCT item_id) AS num_items
    FROM SellerNonFavItems
    GROUP BY seller_id
),
MaxItems AS (
    SELECT MAX(num_items) AS max_num_items
    FROM SellerUniqueItemCounts
)
SELECT S.seller_id, S.num_items
FROM SellerUniqueItemCounts S
JOIN MaxItems M ON S.num_items = M.max_num_items
ORDER BY S.seller_id;
select Products.product_id,
(Products.price + 0.0) * (100 - coalesce(Discounts.discount, 0)) / 100 as final_price,
Products.category
from Products
LEFT OUTER JOIN Discounts
on Products.category = Discounts.category
order by 1
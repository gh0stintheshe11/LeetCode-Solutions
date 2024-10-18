select order_id
from OrdersDetails
group by order_id
having max(quantity) > (select max(av) from (select order_id, avg(quantity) as av from OrdersDetails group by 1) as a)
with cte as (
select *,
SUM(CASE WHEN drink is not null THEN 1 ELSE 0 END) OVER(ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as grp,
ROW_NUMBER() OVER() as rn
from CoffeeShop
)

select id, FIRST_VALUE(drink) OVER(PARTITION BY grp ORDER BY rn) as drink
from cte
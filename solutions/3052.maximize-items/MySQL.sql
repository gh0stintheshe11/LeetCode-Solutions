with type_stats as (
  select
    item_type,
    sum(square_footage) as sum_square,
    count(item_category) as num_category
  from
    inventory
  group by
    1
),
prime as (
  select
    *,
    floor(500000 / sum_square) * num_category as item_count,
    500000 - (floor(500000 / sum_square) * sum_square) as room_for_not_prime
  from
    type_stats
  where
    item_type = 'prime_eligible'
),
not_prime as (
  select
    *,
    floor((select room_for_not_prime from prime) / sum_square) * num_category as item_count
  from
    type_stats
  where
    item_type = 'not_prime'
)
select
  item_type,
  item_count
from
  prime
union all
select
  item_type,
  item_count
from
  not_prime
order by
  item_count desc;
select distinct driver_id, case when b.cnt is null then 0 else b.cnt end as cnt
from Rides a
left join
(
    select passenger_id, count(passenger_id) as cnt
    from Rides
    group by 1
)b
on a.driver_id = b.passenger_id
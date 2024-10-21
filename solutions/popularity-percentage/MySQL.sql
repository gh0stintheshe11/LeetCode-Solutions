with cte as (
    select * from Friends
    union
    select user2, user1 from Friends
)
select user1, round(count(*) / (select count(distinct user1) from cte) * 100, 2) as percentage_popularity
from cte
group by user1
order by user1
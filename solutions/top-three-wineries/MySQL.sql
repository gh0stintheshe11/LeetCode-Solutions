with recursive cte as (
    select 1 rk
    union all
    select rk + 1 from cte where rk < 3
),
cte2 as (
    select * from cte cross join (select distinct country from wineries) t
),
cte3 as (
    select country, concat(winery, ' (', points, ')') winery,
    dense_rank() over (partition by country order by points desc, winery asc) rk 
    from (select country, winery, sum(points) points from wineries group by country, winery) t
)
select country,
    max(case when rk=1 then winery end) top_winery,
    coalesce(max(case when rk=2 then winery end), 'No second winery') second_winery,
    coalesce(max(case when rk=3 then winery end), 'No third winery') third_winery
from cte2 
left join cte3 using(rk, country) 
group by country
order by country
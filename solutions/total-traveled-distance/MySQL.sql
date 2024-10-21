select u.user_id, name, ifnull(sum(distance),0) as 'traveled distance'
from users u
left join rides r
on u.user_id = r.user_id
group by 1
order by 1
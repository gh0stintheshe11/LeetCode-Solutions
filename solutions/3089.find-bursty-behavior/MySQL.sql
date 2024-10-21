select
user_id,
max(rolling_7_cnt) as max_7day_posts,
max(avg_weekly_posts) as avg_weekly_posts
from
(select
user_id, 
post_id,
post_date,
count(post_id)over(partition by user_id order by post_date range between interval 6 day preceding and current row) as rolling_7_cnt,
count(post_id)over(partition by user_id) / 4 as avg_weekly_posts
from Posts
where post_date between '2024-02-01' and '2024-02-28') as t
where rolling_7_cnt >= 2 * avg_weekly_posts
group by user_id
order by user_id
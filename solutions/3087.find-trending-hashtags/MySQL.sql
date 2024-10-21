with feb_hashtags as (
    select
    substring(tweet, locate('#', tweet), 
    locate(' ', concat(tweet, ' '), locate('#', tweet)) - locate('#', tweet)) as hashtag
    from tweets
    where left(tweet_date, 7) LIKE '2024-02'
)
select
hashtag,
count(*) as hashtag_count
from feb_hashtags
group by hashtag
order by hashtag_count desc, hashtag desc
limit 3;
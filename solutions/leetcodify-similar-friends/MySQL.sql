select distinct l1.user_id as user1_id,
                l2.user_id as user2_id
from   listens l1
join   listens l2 
       using(song_id, day)
where  l1.user_id < l2.user_id
       and
       (l1.user_id, l2.user_id)
       in
       (select *
        from   friendship )
group by 1, 2, day
having count(distinct song_id) > 2
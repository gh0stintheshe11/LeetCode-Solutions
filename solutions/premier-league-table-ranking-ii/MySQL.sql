with teams_points as 
(
    select team_id,
    team_name,
    wins * 3 + draws as points
    from TeamStats
),
teams_rk as
(
    select team_id,
    team_name,
    points,
    RANK() over (order by points desc) as position,
    ROW_NUMBER() over (order by points desc) as points_rk
    from teams_points
),
team_ct as 
(
    select
    count(*) as num_teams
    from TeamStats
)
select teams_rk.team_name,
teams_rk.points,
teams_rk.position,
case when teams_rk.position < ((team_ct.num_teams * .33) + 1) then 'Tier 1'
when teams_rk.position < ((team_ct.num_teams * .66) + 1) then 'Tier 2'
else 'Tier 3' end as tier
from teams_rk, team_ct
order by 2 desc, 1
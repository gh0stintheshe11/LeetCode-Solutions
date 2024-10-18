SELECT old.team_id, old.name, 
COALESCE(old.rk, 0) - COALESCE(new.rk, 0) AS rank_diff 
FROM
    (SELECT team_id, name, RANK() OVER(ORDER BY points DESC, name) rk
    FROM teampoints) old
LEFT JOIN
    (SELECT team_id, name, 
    points + points_change, RANK() OVER(ORDER BY points + points_change DESC, name) rk
    FROM teampoints 
    LEFT JOIN pointschange USING(team_id)) new
USING(team_id)
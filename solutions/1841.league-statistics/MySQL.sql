SELECT
    t.team_name,
    IFNULL(SUM(CASE WHEN m.home_team_id IS NOT NULL OR m.away_team_id IS NOT NULL THEN 1 ELSE 0 END), 0) AS matches_played,
    IFNULL(SUM(CASE
        WHEN t.team_id = m.home_team_id AND m.home_team_goals > m.away_team_goals THEN 3
        WHEN t.team_id = m.away_team_id AND m.away_team_goals > m.home_team_goals THEN 3
        WHEN t.team_id = m.home_team_id AND m.home_team_goals = m.away_team_goals THEN 1
        WHEN t.team_id = m.away_team_id AND m.away_team_goals = m.home_team_goals THEN 1
        ELSE 0 END), 0) AS points,
    IFNULL(SUM(CASE WHEN t.team_id = m.home_team_id THEN m.home_team_goals ELSE m.away_team_goals END), 0) AS goal_for,
    IFNULL(SUM(CASE WHEN t.team_id = m.home_team_id THEN m.away_team_goals ELSE m.home_team_goals END), 0) AS goal_against,
    IFNULL(SUM((CASE WHEN t.team_id = m.home_team_id THEN m.home_team_goals ELSE m.away_team_goals END) - (CASE WHEN t.team_id = m.home_team_id THEN m.away_team_goals ELSE m.home_team_goals END)), 0) AS goal_diff
FROM Teams t
LEFT JOIN Matches m ON t.team_id = m.home_team_id OR t.team_id = m.away_team_id
GROUP BY t.team_id, t.team_name
HAVING matches_played > 0
ORDER BY points DESC, goal_diff DESC, t.team_name;
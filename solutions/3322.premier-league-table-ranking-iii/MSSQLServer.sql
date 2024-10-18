WITH RankedTeams AS (
    SELECT 
        season_id,
        team_id,
        team_name,
        (wins * 3 + draws) AS points,
        (goals_for - goals_against) AS goal_difference,
        ROW_NUMBER() OVER (PARTITION BY season_id ORDER BY 
            (wins * 3 + draws) DESC, 
            (goals_for - goals_against) DESC, 
            team_name ASC) AS position
    FROM SeasonStats
)

SELECT 
    season_id,
    team_id,
    team_name,
    points,
    goal_difference,
    position
FROM RankedTeams
ORDER BY 
    season_id ASC, 
    position ASC,
    team_name ASC;
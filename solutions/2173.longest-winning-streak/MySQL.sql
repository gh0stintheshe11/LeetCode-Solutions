# Write your MySQL query statement below

WITH RankedMatches AS (
    SELECT 
        player_id, 
        match_day, 
        result, 
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_day) - 
        ROW_NUMBER() OVER (PARTITION BY player_id, result ORDER BY match_day) AS streak_group
    FROM Matches
),

WinningStreaks AS (
    SELECT 
        player_id, 
        COUNT(*) AS win_streak
    FROM RankedMatches
    WHERE result = 'Win'
    GROUP BY player_id, streak_group
)

SELECT 
    player_id, 
    COALESCE(MAX(win_streak), 0) AS longest_streak
FROM (
    SELECT DISTINCT player_id FROM Matches
) AS Players
LEFT JOIN WinningStreaks USING (player_id)
GROUP BY player_id
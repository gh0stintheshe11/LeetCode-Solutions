SELECT
team_id,
team_name,
3*wins+1*draws+0*losses AS points,
RANK() OVER (ORDER BY (3 * wins + 1 * draws + 0 * losses) DESC) AS position
FROM TeamStats
ORDER BY 3 DESC, 2 ASC
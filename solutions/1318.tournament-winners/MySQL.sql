SELECT final_scores.group_id, MIN(final_scores.player_id) AS player_id
FROM
    (SELECT p.group_id, p.player_id,
            SUM(CASE WHEN p.player_id = m.first_player THEN m.first_score ELSE 0 END +
                CASE WHEN p.player_id = m.second_player THEN m.second_score ELSE 0 END) AS total_score
     FROM Players p
     LEFT JOIN Matches m ON p.player_id = m.first_player OR p.player_id = m.second_player
     GROUP BY p.group_id, p.player_id) AS final_scores
JOIN
    (SELECT group_id, MAX(total_score) AS max_score
     FROM 
        (SELECT p.group_id, p.player_id,
                SUM(CASE WHEN p.player_id = m.first_player THEN m.first_score ELSE 0 END +
                    CASE WHEN p.player_id = m.second_player THEN m.second_score ELSE 0 END) AS total_score
         FROM Players p
         LEFT JOIN Matches m ON p.player_id = m.first_player OR p.player_id = m.second_player
         GROUP BY p.group_id, p.player_id) AS subfinal_scores
     GROUP BY group_id) AS max_scores
ON final_scores.group_id = max_scores.group_id AND final_scores.total_score = max_scores.max_score
GROUP BY final_scores.group_id
ORDER BY final_scores.group_id;
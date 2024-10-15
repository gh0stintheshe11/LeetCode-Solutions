SELECT DISTINCT l.page_id AS recommended_page
FROM Friendship f
JOIN Likes l ON (f.user2_id = l.user_id OR f.user1_id = l.user_id)
WHERE (f.user1_id = 1 OR f.user2_id = 1) 
  AND l.page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1);
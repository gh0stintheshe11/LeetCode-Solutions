SELECT a.user_id AS user1_id, b.user_id AS user2_id
FROM Relations a
JOIN Relations b ON a.follower_id = b.follower_id AND a.user_id < b.user_id
GROUP BY a.user_id, b.user_id
HAVING COUNT(DISTINCT a.follower_id) = (
    SELECT MAX(common_followers) FROM (
        SELECT COUNT(DISTINCT r1.follower_id) AS common_followers
        FROM Relations r1
        JOIN Relations r2 ON r1.follower_id = r2.follower_id AND r1.user_id < r2.user_id
        GROUP BY r1.user_id, r2.user_id
    ) subquery
)
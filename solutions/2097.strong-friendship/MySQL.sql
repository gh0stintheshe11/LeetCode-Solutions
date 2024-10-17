WITH friend AS (
    SELECT user1_id, user2_id
    FROM friendship
    UNION
    SELECT user2_id, user1_id
    FROM friendship
), 
friends_of_friends AS (
    SELECT f1.user1_id, f1.user2_id, f2.user2_id friendfriend_id, f3.user2_id mutualfriend
    FROM friend f1
    JOIN friend f2 ON f1.user2_id = f2.user1_id
                     AND f1.user1_id != f2.user2_id
    JOIN friend f3 ON f1.user1_id = f3.user1_id 
                AND f2.user2_id = f3.user2_id
)
SELECT user1_id, user2_id, COUNT(DISTINCT mutualfriend) common_friend
FROM friends_of_friends ff
WHERE user1_id < user2_id
GROUP BY 1, 2
HAVING COUNT(DISTINCT mutualfriend) >= 3
SELECT t.follower, COUNT(DISTINCT f3.follower) AS num
FROM (
    SELECT DISTINCT f1.follower
    FROM Follow f1
    JOIN Follow f2 ON f1.follower = f2.followee
    ) t
JOIN Follow f3 ON t.follower = f3.followee
GROUP BY t.follower
ORDER BY t.follower;
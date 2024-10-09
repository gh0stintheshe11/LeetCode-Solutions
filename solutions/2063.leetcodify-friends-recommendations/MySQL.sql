WITH CommonSongs AS (
    SELECT a.user_id AS user_a, b.user_id AS user_b, a.day, COUNT(DISTINCT a.song_id) AS common_songs_count
    FROM Listens a
    JOIN Listens b ON a.song_id = b.song_id AND a.day = b.day AND a.user_id < b.user_id
    GROUP BY a.user_id, b.user_id, a.day
    HAVING common_songs_count >= 3
),
NonFriends AS (
    SELECT cs.user_a, cs.user_b
    FROM CommonSongs cs
    LEFT JOIN Friendship f ON (cs.user_a = f.user1_id AND cs.user_b = f.user2_id)
    WHERE f.user1_id IS NULL
)

SELECT DISTINCT user_a AS user_id, user_b AS recommended_id FROM NonFriends
UNION
SELECT DISTINCT user_b AS user_id, user_a AS recommended_id FROM NonFriends;
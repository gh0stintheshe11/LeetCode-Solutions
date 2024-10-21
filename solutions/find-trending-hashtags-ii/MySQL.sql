WITH word AS (
    SELECT
        tweet_id,
        TRIM(
            SUBSTRING_INDEX(
                SUBSTRING_INDEX(tweet, ' ', numbers.n),
                ' ',
                -1
            )
        ) AS word
    FROM (
        SELECT 1 n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
        UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8
        UNION ALL SELECT 9 UNION ALL SELECT 10 UNION ALL SELECT 11 UNION ALL SELECT 12
        UNION ALL SELECT 13 UNION ALL SELECT 14 UNION ALL SELECT 15 UNION ALL SELECT 16
        UNION ALL SELECT 17 UNION ALL SELECT 18 UNION ALL SELECT 19 UNION ALL SELECT 20
        -- Continue adding numbers as needed based on the maximum expected words in a tweet
    ) numbers
    INNER JOIN tweets
        ON CHAR_LENGTH(tweet) - CHAR_LENGTH(REPLACE(tweet, ' ', '')) >= numbers.n - 1
    WHERE
        TRIM(
            SUBSTRING_INDEX(
                SUBSTRING_INDEX(tweet, ' ', numbers.n),
                ' ',
                -1
            )
        ) != ''
    ORDER BY
        tweet_id, numbers.n
)
SELECT word AS hashtag, COUNT(word) AS count
FROM (
    SELECT *
    FROM word
    WHERE word LIKE '#%'
) a
GROUP BY hashtag
ORDER BY COUNT(word) DESC, hashtag DESC
LIMIT 3
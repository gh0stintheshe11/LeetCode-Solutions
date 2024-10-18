SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 140
   OR (char_length(content) - char_length(replace(content, '@', ''))) > 3
   OR (char_length(content) - char_length(replace(content, '#', ''))) > 3
ORDER BY tweet_id;
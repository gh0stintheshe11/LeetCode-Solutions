SELECT post_id, 
       COUNT(DISTINCT sub_id) AS number_of_comments
FROM (
    SELECT DISTINCT sub_id, parent_id
    FROM Submissions
) AS UniqueSubmissions
JOIN (
    SELECT DISTINCT sub_id AS post_id
    FROM Submissions
    WHERE parent_id IS NULL
) AS Posts
ON UniqueSubmissions.parent_id = Posts.post_id
GROUP BY post_id
UNION
SELECT post_id, 0 AS number_of_comments
FROM (
    SELECT DISTINCT sub_id AS post_id
    FROM Submissions
    WHERE parent_id IS NULL
) AS Posts
WHERE post_id NOT IN (
    SELECT DISTINCT parent_id 
    FROM Submissions 
    WHERE parent_id IS NOT NULL
)
ORDER BY post_id;
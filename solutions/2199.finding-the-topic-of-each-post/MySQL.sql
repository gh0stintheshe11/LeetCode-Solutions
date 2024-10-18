WITH
    post_topic AS (
        SELECT
            P.post_id,
            P.content,
            K.topic_id,
            K.word
        FROM
            Posts P
            LEFT JOIN Keywords K 
                ON LOWER(P.content) LIKE CONCAT('% ', LOWER(K.word), ' %')
                OR LOWER(P.content) LIKE CONCAT(LOWER(K.word), ' %')
                OR LOWER(P.content) LIKE CONCAT('% ', LOWER(K.word))
    )
SELECT
    post_id,
    IFNULL(
        GROUP_CONCAT(DISTINCT topic_id ORDER BY topic_id ASC SEPARATOR ','), 'Ambiguous!'
    ) AS topic
FROM
    post_topic
GROUP BY
    post_id
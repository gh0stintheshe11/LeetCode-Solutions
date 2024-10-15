SELECT DISTINCT c.title
FROM TVProgram tp
JOIN Content c
ON tp.content_id = c.content_id
WHERE tp.program_date BETWEEN '2020-06-01' AND '2020-06-30'
AND c.Kids_content = 'Y'
AND c.content_type = 'Movies';
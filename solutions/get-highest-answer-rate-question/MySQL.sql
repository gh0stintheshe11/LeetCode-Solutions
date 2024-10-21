SELECT question_id AS survey_log
FROM (
    SELECT question_id, 
           COUNT(CASE WHEN action = 'answer' THEN 1 END) / COUNT(CASE WHEN action = 'show' THEN 1 END) AS answer_rate
    FROM SurveyLog
    GROUP BY question_id
) AS rates
ORDER BY answer_rate DESC, question_id ASC
LIMIT 1;
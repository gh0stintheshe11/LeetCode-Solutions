SELECT DISTINCT e.user_id
FROM emails e
JOIN texts t ON e.email_id = t.email_id
WHERE t.signup_action = 'Verified'
AND DATE(t.action_date) = DATE_ADD(DATE(e.signup_date), INTERVAL 1 DAY)
ORDER BY e.user_id;
WITH UserCalls AS (
    SELECT caller_id AS user_id, recipient_id, call_time
    FROM Calls
    UNION ALL
    SELECT recipient_id AS user_id, caller_id AS recipient_id, call_time
    FROM Calls
),
MinMaxCalls AS (
    SELECT 
        user_id, 
        DATE(call_time) AS call_date, 
        MIN(call_time) AS first_call_time, 
        MAX(call_time) AS last_call_time
    FROM UserCalls
    GROUP BY user_id, DATE(call_time)
),
FirstLastRecipient AS (
    SELECT 
        m.user_id, 
        m.call_date,
        (SELECT recipient_id FROM UserCalls WHERE user_id = m.user_id AND call_time = m.first_call_time) AS first_recipient,
        (SELECT recipient_id FROM UserCalls WHERE user_id = m.user_id AND call_time = m.last_call_time) AS last_recipient
    FROM MinMaxCalls m
)
SELECT DISTINCT user_id
FROM FirstLastRecipient
WHERE first_recipient = last_recipient;
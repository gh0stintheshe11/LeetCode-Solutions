SELECT 
    SUBSTRING_INDEX(email, '@', -1) AS email_domain, 
    COUNT(*) AS count
FROM 
    Emails
WHERE 
    email LIKE '%.com'
GROUP BY 
    email_domain
ORDER BY 
    email_domain ASC;
SELECT DISTINCT a.user_id
FROM Loans a
JOIN Loans b ON a.user_id = b.user_id
WHERE a.loan_type = 'Refinance' AND b.loan_type = 'Mortgage'
ORDER BY a.user_id;
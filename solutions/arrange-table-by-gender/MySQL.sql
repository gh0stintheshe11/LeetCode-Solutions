SELECT user_id, gender
FROM (
    SELECT user_id, gender, ROW_NUMBER() OVER (PARTITION BY gender ORDER BY user_id) as rn
    FROM Genders
) AS ordered_genders
ORDER BY rn, 
         CASE 
             WHEN gender = 'female' THEN 1
             WHEN gender = 'other' THEN 2
             WHEN gender = 'male' THEN 3
         END;
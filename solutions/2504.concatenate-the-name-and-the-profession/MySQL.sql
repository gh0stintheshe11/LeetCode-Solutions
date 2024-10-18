SELECT 
    person_id,
    CONCAT(name, '(', LEFT(profession, 1), ')') AS name
FROM 
    Person
ORDER BY 
    person_id DESC;
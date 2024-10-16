CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    DECLARE @nthHighestSalary INT;
    
    WITH SortedSalaries AS (
        SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
        FROM Employee
    )
    SELECT @nthHighestSalary = salary
    FROM SortedSalaries
    WHERE rank = @N;
    
    RETURN @nthHighestSalary;
END
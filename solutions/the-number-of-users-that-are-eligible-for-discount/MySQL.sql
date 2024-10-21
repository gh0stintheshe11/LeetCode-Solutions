CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
    SELECT COUNT(DISTINCT user_id) FROM Purchases
    WHERE time_stamp >= startDate AND time_stamp <= endDate
    AND amount >= minAmount
  );
END
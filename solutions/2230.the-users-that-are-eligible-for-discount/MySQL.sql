CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
  select distinct user_id
  from purchases
  where time_stamp between startDate and endDate
  and amount >= minAmount
  order by 1;
END
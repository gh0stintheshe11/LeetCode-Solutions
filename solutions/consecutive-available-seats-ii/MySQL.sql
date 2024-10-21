WITH CTE AS (
  SELECT 
    seat_id,
    free,
    CASE WHEN free = 1 THEN @running_sum ELSE (@running_sum := @running_sum + 1) END AS group_id,
    @running_sum := CASE WHEN free = 0 THEN @running_sum + 1 ELSE @running_sum END
  FROM 
    Cinema, (SELECT @running_sum := 0) r
  ORDER BY seat_id
)

SELECT 
  MIN(seat_id) AS first_seat_id, 
  MAX(seat_id) AS last_seat_id, 
  COUNT(seat_id) AS consecutive_seats_len
FROM 
  CTE
WHERE 
  free = 1
GROUP BY 
  group_id
HAVING 
  COUNT(seat_id) = (
    SELECT MAX(count_seat)
    FROM (
      SELECT COUNT(seat_id) AS count_seat
      FROM CTE
      WHERE free = 1
      GROUP BY group_id
    ) sub
  )
ORDER BY
  first_seat_id;
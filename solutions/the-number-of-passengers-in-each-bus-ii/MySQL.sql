WITH RECURSIVE cte AS (
    SELECT 
        b.bus_id,
        b.capacity,
        COUNT(p.passenger_id) AS p_count,
        ROW_NUMBER() OVER(ORDER BY b.arrival_time ASC) AS rankin,
        b.arrival_time
    FROM Buses b
    LEFT JOIN Passengers p ON b.arrival_time >= p.arrival_time
    GROUP BY b.bus_id, b.capacity
),
cte2 AS (
      SELECT 
            bus_id,capacity,
            IFNULL(p_count-(LAG(p_count) OVER()),p_count) AS diff, 
            rankin
      FROM cte
),
cte3 AS (
      SELECT 
            bus_id, 
            LEAST(capacity,diff) AS boarded, 
            GREATEST(0, diff-capacity) AS remain, 
            rankin
      FROM cte2
      WHERE rankin = 1
      UNION ALL
      SELECT 
            c2.bus_id, 
            LEAST(capacity, diff+c3.remain) AS boarded, 
            GREATEST(0, diff+c3.remain-capacity) AS remain, 
            c2.rankin
      FROM cte2 c2 JOIN cte3 c3
      ON c2.rankin = c3.rankin+1
)

SELECT bus_id, boarded AS passengers_cnt FROM cte3 ORDER BY bus_id
# Write your MySQL query statement below

SELECT 
    car_id, 
    ROUND(SUM(fee_paid), 2) AS total_fee_paid,
    ROUND(SUM(fee_paid) / SUM(TIMESTAMPDIFF(MINUTE, entry_time, exit_time) / 60), 2) AS avg_hourly_fee,
    (
        SELECT lot_id 
        FROM (
                SELECT lot_id, 
                       SUM(TIMESTAMPDIFF(SECOND, entry_time, exit_time)) AS total_seconds 
                FROM ParkingTransactions pt 
                WHERE pt.car_id = p.car_id
                GROUP BY lot_id 
                ORDER BY total_seconds DESC, lot_id
                LIMIT 1
             ) AS subquery
    ) AS most_time_lot
FROM ParkingTransactions p
GROUP BY car_id
ORDER BY car_id;
WITH ES_overlap_raw AS (
    SELECT ES1.employee_id, ES1.start_time, ES1.end_time,
    ES2.start_time AS later_shift_start_time,
    ES2.end_time AS later_shift_end_time
    FROM EmployeeShifts ES1,
    EmployeeShifts ES2
    WHERE ES1.employee_id = ES2.employee_id
    AND ES2.start_time > ES1.start_time
    AND ES2.start_time < ES1.end_time
),
ES_overlap_group AS (
    SELECT employee_id,
    start_time,
    end_time,
    COUNT(*) AS overlap_ct,
    MIN(later_shift_start_time) AS overlap_start,
    MAX(later_shift_end_time) AS overlap_end
    FROM ES_overlap_raw
    GROUP BY employee_id,
    start_time,
    end_time
),
ES_overlap_mins AS (
    SELECT employee_id,
    SUM(TIMESTAMPDIFF(MINUTE, later_shift_start_time, LEAST(later_shift_end_time, end_time))) AS overlap_mins
    FROM ES_overlap_raw
    GROUP BY employee_id
),
ES_overlap_max_ct AS (
    SELECT employee_id,
    MAX(overlap_ct) AS max_overlap_ct
    FROM ES_overlap_group
    GROUP BY employee_id
)
SELECT ES_overlap_mins.employee_id,
ES_overlap_max_ct.max_overlap_ct + 1 AS max_overlapping_shifts,
ES_overlap_mins.overlap_mins AS total_overlap_duration
FROM ES_overlap_mins,
ES_overlap_max_ct
WHERE ES_overlap_mins.employee_id = ES_overlap_max_ct.employee_id
UNION
SELECT DISTINCT employee_id, 1, 0
FROM EmployeeShifts
WHERE NOT EXISTS (SELECT * FROM ES_overlap_raw
WHERE ES_overlap_raw.employee_id = EmployeeShifts.employee_id)
ORDER BY 1
with t1 as (
    select a.employee_id, a.task_id, (select 1 + count(*) from Tasks b where b.start_time < a.start_time and b.end_time > a.start_time and b.employee_id = a.employee_id) as cnt
    from Tasks a
), t2 as (
    select employee_id, start_time as time, 1 as cnt from Tasks
    union all
    select employee_id, end_time as time, -1 as cnt from Tasks
), t3 as (
    select employee_id, time, rank() over (partition by employee_id order by time, cnt) as r, sum(cnt) over (partition by employee_id order by time, cnt) as cur from t2
), t4 as (
    select a.employee_id, floor(sum(TIME_TO_SEC(TIMEDIFF(b.time, a.time)))/3600) as hours
    from t3 as a, t3 as b
    where a.cur != 0 and b.r = a.r + 1 and a.employee_id = b.employee_id
    group by a.employee_id
)

select t1.employee_id, t4.hours as total_task_hours, max(t1.cnt) as max_concurrent_tasks 
from t1, t4
where t1.employee_id = t4.employee_id
group by employee_id
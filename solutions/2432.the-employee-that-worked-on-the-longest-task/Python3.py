class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = 0
        result_id = None
        last_leave_time = 0
        
        for employee_id, leave_time in logs:
            task_duration = leave_time - last_leave_time
            if task_duration > max_time or (task_duration == max_time and (result_id is None or employee_id < result_id)):
                max_time = task_duration
                result_id = employee_id
            last_leave_time = leave_time
        
        return result_id
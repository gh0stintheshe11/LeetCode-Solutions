from typing import List
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_done_day = {}
        current_day = 0
        
        for task in tasks:
            current_day += 1
            if task in last_done_day:
                last_day = last_done_day[task]
                if current_day - last_day <= space:
                    current_day = last_day + space + 1
            
            last_done_day[task] = current_day
        
        return current_day
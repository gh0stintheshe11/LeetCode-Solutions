from functools import lru_cache
from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        
        @lru_cache(None)
        def dfs(mask: int, remaining_time: int) -> int:
            if mask == 0:
                return 0
            
            result = float('inf')
            new_mask = mask
            for i in range(n):
                if mask & (1 << i):
                    # If we can fit the current task in the remaining time
                    if tasks[i] <= remaining_time:
                        result = min(result, dfs(mask ^ (1 << i), remaining_time - tasks[i]))
                    else:
                        # Start a new session because the current task cannot fit in the remaining time
                        result = min(result, dfs(mask ^ (1 << i), sessionTime - tasks[i]) + 1)
            
            return result
        
        return dfs((1 << n) - 1, sessionTime) + 1
from typing import List

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        from functools import lru_cache

        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(state):
            if state == 0:
                return 0

            min_operations = float('inf')
            for i in range(m):
                for j in range(n):
                    if state & (1 << (i * n + j)):
                        new_state = state
                        for x in range(n):
                            new_state &= ~(1 << (i * n + x))
                        for y in range(m):
                            new_state &= ~(1 << (y * n + j))
                        min_operations = min(min_operations, 1 + dfs(new_state))
            return min_operations
        
        initial_state = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    initial_state |= (1 << (i * n + j))
                    
        return dfs(initial_state)
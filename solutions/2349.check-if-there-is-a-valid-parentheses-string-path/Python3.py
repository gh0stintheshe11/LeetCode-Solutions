from typing import List
from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        @lru_cache(None)
        def dfs(i: int, j: int, balance: int) -> bool:
            if balance < 0:
                return False
            if i == m - 1 and j == n - 1:
                return balance == 0

            if i + 1 < m and dfs(i + 1, j, balance + (1 if grid[i + 1][j] == '(' else -1)):
                return True
            if j + 1 < n and dfs(i, j + 1, balance + (1 if grid[i][j + 1] == '(' else -1)):
                return True

            return False

        if grid[0][0] == '(':
            return dfs(0, 0, 1)
        return False
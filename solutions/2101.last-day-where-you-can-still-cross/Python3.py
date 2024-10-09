from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def canCross(day):
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            def dfs(r, c):
                if r == row - 1:
                    return True
                grid[r][c] = 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        if dfs(nr, nc):
                            return True
                return False
            
            for c in range(col):
                if grid[0][c] == 0 and dfs(0, c):
                    return True
            return False

        left, right = 0, len(cells) - 1
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canCross(mid + 1):
                answer = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        
        return answer
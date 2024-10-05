from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def canReachDestination(mid: int) -> bool:
            rows, cols = len(heights), len(heights[0])
            visited = [[False] * cols for _ in range(rows)]
            min_heap = [(0, 0, 0)]  # (effort, row, col)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            while min_heap:
                effort, x, y = heappop(min_heap)
                if x == rows - 1 and y == cols - 1:
                    return True
                if visited[x][y]:
                    continue
                visited[x][y] = True
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                        current_effort = abs(heights[nx][ny] - heights[x][y])
                        if current_effort <= mid:
                            heappush(min_heap, (current_effort, nx, ny))
            return False
        
        left, right = 0, max(max(row) for row in heights) - min(min(row) for row in heights)
        while left < right:
            mid = (left + right) // 2
            if canReachDestination(mid):
                right = mid
            else:
                left = mid + 1
        return left

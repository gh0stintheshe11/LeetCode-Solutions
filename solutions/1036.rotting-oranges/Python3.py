from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Initialize the queue for BFS and count fresh oranges
        queue = deque()
        fresh_count = 0
        
        # Populate the queue with the initial positions of rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # If there are no fresh oranges, return 0
        if fresh_count == 0:
            return 0
        
        # Directions for moving up, down, left, right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize the minutes counter
        minutes = 0
        
        # Perform BFS
        while queue:
            # Process all the rotten oranges at the current minute
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                # Check all 4-directionally adjacent cells
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    # If the adjacent cell is a fresh orange, it becomes rotten
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_count -= 1
            
            # Increment the minutes counter if there are still oranges to process
            if queue:
                minutes += 1
        
        # If there are still fresh oranges left, return -1
        return -1 if fresh_count > 0 else minutes
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        
        # Initialize the queue for BFS with (row, col, remaining k)
        queue = deque([(0, 0, k)])
        visited = {(0, 0, k)}
        
        # Define directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Steps counter
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                x, y, remaining = queue.popleft()
                
                # Explore the neighbors
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    # Check if reached the target
                    if nx == m - 1 and ny == n - 1:
                        return steps + 1
                    
                    # Check boundaries
                    if 0 <= nx < m and 0 <= ny < n:
                        new_k = remaining - grid[nx][ny]
                        
                        # If there's enough remaining k to traverse
                        if new_k >= 0 and (nx, ny, new_k) not in visited:
                            visited.add((nx, ny, new_k))
                            queue.append((nx, ny, new_k))
            
            steps += 1
        
        return -1
from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(start, goal):
            if start == goal:
                return 0
            rows, cols = len(forest), len(forest[0])
            queue = deque([start])
            visited = set([start])
            steps = 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while queue:
                steps += 1
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and forest[nx][ny] != 0:
                            if (nx, ny) == goal:
                                return steps
                            queue.append((nx, ny))
                            visited.add((nx, ny))
            return -1
        
        # Collect all tree positions and sort them by height
        trees = sorted((h, r, c) for r, row in enumerate(forest) for c, h in enumerate(row) if h > 1)
        
        # Start from (0, 0)
        start = (0, 0)
        total_steps = 0
        
        for height, x, y in trees:
            steps = bfs(start, (x, y))
            if steps == -1:
                return -1
            total_steps += steps
            start = (x, y)
        
        return total_steps
from typing import List
from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def roll(x, y, dx, dy):
            while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
            return (x, y)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([tuple(start)])
        visited = set()
        visited.add(tuple(start))
        
        while queue:
            x, y = queue.popleft()
            if [x, y] == destination:
                return True
            for dx, dy in directions:
                new_x, new_y = roll(x, y, dx, dy)
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
                    
        return False
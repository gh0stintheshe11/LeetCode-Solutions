from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Normalize the position to the first quadrant
        x, y = abs(x), abs(y)
        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), 
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        queue = deque([(0, 0, 0)])  # (x, y, steps)
        visited = set([(0, 0)])
        
        while queue:
            cur_x, cur_y, steps = queue.popleft()
            if (cur_x, cur_y) == (x, y):
                return steps
            
            for dx, dy in directions:
                next_x, next_y = cur_x + dx, cur_y + dy
                if (next_x, next_y) not in visited and -2 <= next_x <= x + 2 and -2 <= next_y <= y + 2:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, steps + 1))
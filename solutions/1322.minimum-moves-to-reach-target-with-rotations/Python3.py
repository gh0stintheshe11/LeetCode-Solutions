from collections import deque
from typing import List, Tuple

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        target = (n - 1, n - 2, 0)  # (r, c, orientation) -> orientation: 0 for horizontal, 1 for vertical
        start = (0, 0, 0)
        
        # BFS queue
        queue = deque([start])
        visited = set([start])
        moves = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c, orientation = queue.popleft()
                
                # Check if reached target
                if (r, c, orientation) == target:
                    return moves
                
                # Add possible moves
                if orientation == 0:  # Horizontal (r, c) -> (r, c+1)
                    # Move right
                    if c + 2 < n and grid[r][c + 2] == 0 and (r, c + 1, 0) not in visited:
                        visited.add((r, c + 1, 0))
                        queue.append((r, c + 1, 0))
                    # Move down
                    if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0 and (r + 1, c, 0) not in visited:
                        visited.add((r + 1, c, 0))
                        queue.append((r + 1, c, 0))
                    # Rotate clockwise
                    if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0 and (r, c, 1) not in visited:
                        visited.add((r, c, 1))
                        queue.append((r, c, 1))
                else:  # Vertical (r, c) -> (r+1, c)
                    # Move right
                    if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0 and (r, c + 1, 1) not in visited:
                        visited.add((r, c + 1, 1))
                        queue.append((r, c + 1, 1))
                    # Move down
                    if r + 2 < n and grid[r + 2][c] == 0 and (r + 1, c, 1) not in visited:
                        visited.add((r + 1, c, 1))
                        queue.append((r + 1, c, 1))
                    # Rotate counter-clockwise
                    if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0 and (r, c, 0) not in visited:
                        visited.add((r, c, 0))
                        queue.append((r, c, 0))
            
            moves += 1
        
        return -1
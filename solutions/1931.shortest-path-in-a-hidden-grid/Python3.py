from collections import deque

# Mapping directions to their reverses and to dx, dy moves
DIRS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
REV_DIRS = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        # DFS to map the reachable area
        def dfs(x, y):
            if master.isTarget():
                nonlocal target
                target = (x, y)
            
            for direction, (dx, dy) in DIRS.items():
                nx, ny = x + dx, y + dy
                if (nx, ny) not in grid and master.canMove(direction):
                    master.move(direction)
                    grid.add((nx, ny))
                    dfs(nx, ny)
                    master.move(REV_DIRS[direction])

        target = None
        grid = set()
        grid.add((0, 0))
        dfs(0, 0)

        if target is None:
            return -1

        # BFS to find the shortest path to the target
        queue = deque([(0, 0, 0)])  # (x, y, steps)
        visited = set((0, 0))
        
        while queue:
            x, y, steps = queue.popleft()
            if (x, y) == target:
                return steps
            for dx, dy in DIRS.values():
                nx, ny = x + dx, y + dy
                if (nx, ny) in grid and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
        
        return -1
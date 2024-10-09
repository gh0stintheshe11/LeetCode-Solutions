from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findShortestPath(self, master: 'GridMaster') -> int:
        directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        reverse = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        
        START = (0, 0)
        TARGET = None
        
        # Discovered grid with costs, initially set to None for unexplored cells
        grid = {}

        # Function to perform DFS and map out the grid
        def dfs(x, y):
            nonlocal TARGET
            if master.isTarget():
                TARGET = (x, y)
            
            for direction, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if (nx, ny) not in grid:  # Means unexplored cell
                    if master.canMove(direction):
                        cost = master.move(direction)
                        grid[(nx, ny)] = cost
                        dfs(nx, ny)
                        master.move(reverse[direction])  # move back

        # Start the exploration
        grid[START] = 0
        dfs(*START)
        
        # Check if target was discovered
        if TARGET is None:
            return -1
        
        # Dijkstra's algorithm initialization
        pq = [(0, *START)]
        dist = {START: 0}
        
        # Dijkstra's algorithm to find the minimum cost path to target
        while pq:
            current_cost, x, y = heappop(pq)
            if (x, y) == TARGET:
                return current_cost
            
            for direction, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if (nx, ny) in grid:
                    step_cost = grid[(nx, ny)]
                    new_cost = current_cost + step_cost
                    if (nx, ny) not in dist or new_cost < dist[(nx, ny)]:
                        dist[(nx, ny)] = new_cost
                        heappush(pq, (new_cost, nx, ny))
        
        return -1
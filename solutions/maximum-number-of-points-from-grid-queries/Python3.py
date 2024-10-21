from typing import List
from heapq import heappush, heappop

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        # Directions for exploring neighboring cells
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Sort queries and keep track of original indices
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        # Prepare result array
        result = [0] * len(queries)
        
        # Min-heap to keep track of reachable cells in the grid
        heap = [(grid[0][0], 0, 0)]
        
        # Visited set to avoid reprocessing the same cell
        visited = set()
        visited.add((0, 0))
        
        # Current count of reachable points
        current_points = 0
        
        # Process each query in sorted order
        for value, index in sorted_queries:
            # Process all cells that can be reached with this query value
            while heap and heap[0][0] < value:
                cell_value, x, y = heappop(heap)
                current_points += 1
                # Explore the neighboring cells
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        heappush(heap, (grid[nx][ny], nx, ny))
            
            # Store result for this query
            result[index] = current_points
        
        return result
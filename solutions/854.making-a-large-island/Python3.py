from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Function to perform DFS and mark the island with a unique ID
        def dfs(x, y, island_id):
            stack = [(x, y)]
            island_size = 0
            while stack:
                cx, cy = stack.pop()
                if 0 <= cx < n and 0 <= cy < n and grid[cx][cy] == 1 and (cx, cy) not in visited:
                    visited.add((cx, cy))
                    island_sizes[(cx, cy)] = island_id
                    island_size += 1
                    stack.extend([(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)])
            return island_size
        
        visited = set()
        island_id_counter = 2
        island_sizes = {}
        id_to_size = {}
        
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1 and (x, y) not in visited:
                    size = dfs(x, y, island_id_counter)
                    id_to_size[island_id_counter] = size
                    island_id_counter += 1
        
        if not id_to_size:
            return 1
        
        max_island_size = max(id_to_size.values())
        
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    neighbors = set()
                    new_island_size = 1
                    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) in island_sizes:
                            neighbor_id = island_sizes[(nx, ny)]
                            neighbors.add(neighbor_id)
                    for neighbor_id in neighbors:
                        new_island_size += id_to_size[neighbor_id]
                    max_island_size = max(max_island_size, new_island_size)
        
        return max_island_size
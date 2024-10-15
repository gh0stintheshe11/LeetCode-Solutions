from typing import List
from collections import deque

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        low, high = pricing
        start_row, start_col = start

        # Direction vectors for moving up, down, left, or right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        queue = deque([(start_row, start_col, 0)]) # (row, col, distance)
        visited[start_row][start_col] = True
        result = []

        while queue:
            row, col, dist = queue.popleft()
            price = grid[row][col]

            # Check if this is an item within the required price range
            if low <= price <= high:
                result.append((dist, price, row, col))

            # Explore neighboring cells in 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and not visited[new_row][new_col]:
                    if grid[new_row][new_col] != 0:  # Not a wall
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col, dist + 1))

        # Sort result according to the ranking criteria given
        result.sort()
        
        # Extract the coordinate pairs and return the top k items
        return [[r, c] for _, _, r, c in result[:k]]
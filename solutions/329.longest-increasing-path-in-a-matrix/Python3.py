from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        cache = [[-1] * n for _ in range(m)]
        
        def dfs(x, y):
            if cache[x][y] != -1:
                return cache[x][y]
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            max_path = 1
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    max_path = max(max_path, 1 + dfs(nx, ny))
            
            cache[x][y] = max_path
            return max_path
        
        longest_path = 0
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i, j))
        
        return longest_path
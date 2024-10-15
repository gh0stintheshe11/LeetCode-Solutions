from typing import List

class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        def can_match(boy: int, visited: List[bool]) -> bool:
            for girl in range(n):
                if grid[boy][girl] and not visited[girl]:
                    visited[girl] = True
                    if girl_mapping[girl] == -1 or can_match(girl_mapping[girl], visited):
                        girl_mapping[girl] = boy
                        return True
            return False
        
        m, n = len(grid), len(grid[0])
        girl_mapping = [-1] * n
        result = 0
        
        for boy in range(m):
            visited = [False] * n
            if can_match(boy, visited):
                result += 1
                
        return result
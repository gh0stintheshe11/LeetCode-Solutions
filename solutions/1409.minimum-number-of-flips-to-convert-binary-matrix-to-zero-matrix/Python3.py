from collections import deque
from typing import List

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        def mat_to_int(mat):
            result = 0
            for i in range(m):
                for j in range(n):
                    result |= (mat[i][j] << (i * n + j))
            return result
        
        def flip(state, i, j):
            for di, dj in [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    state ^= (1 << (ni * n + nj))
            return state
        
        initial_state = mat_to_int(mat)
        queue = deque([(initial_state, 0)])
        visited = set([initial_state])

        while queue:
            current_state, step = queue.popleft()
            if current_state == 0:
                return step
            
            for i in range(m):
                for j in range(n):
                    next_state = flip(current_state, i, j)
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, step + 1))
        
        return -1
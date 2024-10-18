from typing import List
from collections import defaultdict
import heapq

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                heapq.heappush(diagonals[i - j], mat[i][j])
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = heapq.heappop(diagonals[i - j])
        
        return mat
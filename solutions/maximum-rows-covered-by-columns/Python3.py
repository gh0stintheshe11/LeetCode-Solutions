from typing import List
from itertools import combinations

class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        max_covered_rows = 0
        
        for cols in combinations(range(n), numSelect):
            covered_rows = 0
            for i in range(m):
                if all(matrix[i][j] == 0 or j in cols for j in range(n)):
                    covered_rows += 1
            max_covered_rows = max(max_covered_rows, covered_rows)
        
        return max_covered_rows
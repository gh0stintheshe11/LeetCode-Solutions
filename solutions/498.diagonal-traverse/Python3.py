from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        for d in range(m + n - 1):
            intermediate = []
            
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            
            while r < m and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
                
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        
        return result
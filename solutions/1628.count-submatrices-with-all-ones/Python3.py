from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        result = 0
        
        for start_row in range(m):
            height = [1] * n
            
            for row in range(start_row, m):
                for col in range(n):
                    height[col] &= mat[row][col]
                
                min_height = 0
                for col in range(n):
                    if height[col] == 1:
                        min_height += 1
                        result += min_height
                    else:
                        min_height = 0
  
        return result
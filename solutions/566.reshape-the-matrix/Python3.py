from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        flat = [num for row in mat for num in row]
        return [flat[i * c:(i + 1) * c] for i in range(r)]
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_count = [0] * m
        col_count = [0] * n
        
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1
        
        odd_cells = 0
        for i in range(m):
            for j in range(n):
                if (row_count[i] + col_count[j]) % 2 == 1:
                    odd_cells += 1
        
        return odd_cells
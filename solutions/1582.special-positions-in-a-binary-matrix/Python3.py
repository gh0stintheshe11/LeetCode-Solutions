class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        
        row_ones = [0] * rows
        col_ones = [0] * cols
        
        # Count the number of 1's in each row and column
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    row_ones[r] += 1
                    col_ones[c] += 1
        
        # Calculate special positions
        special_count = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and row_ones[r] == 1 and col_ones[c] == 1:
                    special_count += 1
                    
        return special_count
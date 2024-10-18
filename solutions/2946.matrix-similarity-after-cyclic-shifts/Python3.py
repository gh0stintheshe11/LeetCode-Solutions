class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n
        
        for i, row in enumerate(mat):
            if i % 2 == 0:  # even-indexed rows
                shifted_row = row[k:] + row[:k]
            else:  # odd-indexed rows
                shifted_row = row[-k:] + row[:-k]
            
            if shifted_row != row:
                return False
        
        return True
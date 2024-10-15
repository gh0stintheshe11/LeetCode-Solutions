class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        valid_set = set(range(1, n + 1))
        
        for i in range(n):
            if set(matrix[i]) != valid_set:
                return False
            if set(matrix[j][i] for j in range(n)) != valid_set:
                return False
        
        return True
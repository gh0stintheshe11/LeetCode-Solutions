class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        # Get dimensions of the matrix
        m = len(matrix)
        n = len(matrix[0])
        
        # Find maximum in each column
        max_in_column = [-float('inf')] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != -1:
                    max_in_column[j] = max(max_in_column[j], matrix[i][j])
        
        # Replace -1 with the column max
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_in_column[j]
        
        return matrix
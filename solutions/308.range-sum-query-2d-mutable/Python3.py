class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.bit = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        self.nums = [[0] * self.n for _ in range(self.m)]
        
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
        
    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += delta
                j += (j & -j)
            i += (i & -i)
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._sum(row2 + 1, col2 + 1) - self._sum(row2 + 1, col1) - self._sum(row1, col2 + 1) + self._sum(row1, col1)
    
    def _sum(self, row: int, col: int) -> int:
        sum_val = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                sum_val += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return sum_val
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        prefSum = [[0] * (n + 1) for _ in range(n)]
        for col in range(n):
            for row in range(1, n + 1):
                prefSum[col][row] = prefSum[col][row - 1] + grid[row - 1][col]
        prevColWith = [0] * (n + 1)
        prevColEx = [0] * (n + 1)
        for i in range(1, n):
            colWith = [0] * (n + 1)
            colEx = [0] * (n + 1) 
            for pb in range(n + 1):
                for cb in range(n + 1):
                    if pb >= cb:
                        colWith[cb] = max(
                            colWith[cb], 
                            prevColWith[pb] + prefSum[i][pb] - prefSum[i][cb])
                        colEx[cb] = max(colEx[cb], prevColWith[pb])
                    else:
                        colWith[cb] = max(
                            colWith[cb], 
                            prevColEx[pb] + prefSum[i - 1][cb] - prefSum[i - 1][pb])
                        colEx[cb] = max(
                            colEx[cb], 
                            prevColEx[pb] + prefSum[i - 1][cb] - prefSum[i - 1][pb])
            prevColWith = colWith
            prevColEx = colEx
        return max(prevColWith)
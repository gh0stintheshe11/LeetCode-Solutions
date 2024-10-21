class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n): 
                prefix[i+1][j+1] = grid[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
        
        seen = [[0]*n for _ in range(m)]
        for i in range(m-stampHeight+1): 
            for j in range(n-stampWidth+1): 
                diff = prefix[i+stampHeight][j+stampWidth] - prefix[i+stampHeight][j] - prefix[i][j+stampWidth] + prefix[i][j]
                if diff == 0: seen[i][j] = 1
                    
        prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m): 
            for j in range(n): 
                prefix[i+1][j+1] = seen[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
                
        for i in range(m):
            ii = max(0, i-stampHeight+1)
            for j in range(n): 
                jj = max(0, j-stampWidth+1)
                if grid[i][j] == 0 and prefix[i+1][j+1] - prefix[i+1][jj] - prefix[ii][j+1] + prefix[ii][jj] == 0: return False 
        return True
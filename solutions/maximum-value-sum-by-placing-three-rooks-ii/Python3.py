def fmax(a, b):
    return a if a > b else b
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        ans = -10**15
        def solve():
            n = len(board)
            m = len(board[0])
            ans = -10**15
            dp = [[-10**15]*m for _ in range(n)]
            # calculate partial max for corners, rows and columns
            pmax = [list(board[i]) for i in range(n)]
            rmax = [list(board[i]) for i in range(n)]
            cmax = [list(board[i]) for i in range(n)]
            for i in range(n):
                for j in range(m):
                    if i>0:
                        pmax[i][j] = fmax(pmax[i][j], pmax[i-1][j])
                        cmax[i][j] = fmax(cmax[i][j], cmax[i-1][j])
                    if j>0:
                        pmax[i][j] = fmax(pmax[i][j], pmax[i][j-1])
                        rmax[i][j] = fmax(rmax[i][j], rmax[i][j-1])
            # bruteforce third rook while calculating dp of the corner for the other two
            for i in range(2, n):
                for j in range(2, m):
                    dp[i][j] = fmax(dp[i][j], pmax[i-2][j-2] + board[i-1][j-1])
                    dp[i][j] = fmax(dp[i][j], rmax[i-1][j-2] + cmax[i-2][j-1])
                    if i > 2:
                        dp[i][j] = fmax(dp[i][j], dp[i-1][j])
                    if j > 2:
                        dp[i][j] = fmax(dp[i][j], dp[i][j-1])
                    ans = fmax(ans, board[i][j] + dp[i][j])
            return ans
        
        def rotate():
            # rotate the board 180 degrees
            n = len(board)
            m = len(board[0])
            for i in range(n//2):
                for j in range(m):
                    board[i][j], board[n-i-1][m-j-1] = board[n-i-1][m-j-1], board[i][j]
            if n % 2 == 1:
                i = n//2
                for j in range(m//2):
                    board[i][j], board[n-i-1][m-j-1] = board[n-i-1][m-j-1], board[i][j]
        
        def flip():
            # flip the board
            n = len(board)
            m = len(board[0])
            for i in range(n//2):
                for j in range(m):
                    board[i][j], board[n-i-1][j] = board[n-i-1][j], board[i][j]
        
        # calculate the answer for each corner
        ans = fmax(ans, solve())
        rotate()
        ans = fmax(ans, solve())
        flip()
        ans = fmax(ans, solve())
        rotate()
        ans = fmax(ans, solve())
        return ans
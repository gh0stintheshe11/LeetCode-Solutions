class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        
        while True:
            crush = set()
            
            # Find candies to crush horizontally
            for i in range(m):
                for j in range(n-2):
                    if board[i][j] and board[i][j] == board[i][j+1] == board[i][j+2]:
                        crush.update({(i, j), (i, j+1), (i, j+2)})
            
            # Find candies to crush vertically
            for i in range(m-2):
                for j in range(n):
                    if board[i][j] and board[i][j] == board[i+1][j] == board[i+2][j]:
                        crush.update({(i, j), (i+1, j), (i+2, j)})
            
            if not crush:
                break
            
            for i, j in crush:
                board[i][j] = 0
            
            # Apply gravity
            for j in range(n):
                idx = m-1
                for i in range(m-1, -1, -1):
                    if board[i][j] != 0:
                        board[idx][j] = board[i][j]
                        if idx != i:
                            board[i][j] = 0
                        idx -= 1
        
        return board
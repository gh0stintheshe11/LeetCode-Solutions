from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def countMines(board, x, y):
            mines = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
                        if board[x + i][y + j] == 'M':
                            mines += 1
            return mines
        
        def dfs(board, x, y):
            if board[x][y] != 'E':
                return
            mines = countMines(board, x, y)
            if mines == 0:
                board[x][y] = 'B'
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
                            dfs(board, x + i, y + j)
            else:
                board[x][y] = str(mines)
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            dfs(board, x, y)
        
        return board
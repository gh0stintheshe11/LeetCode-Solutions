from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(char):
            for i in range(3):
                if all(board[i][j] == char for j in range(3)): return True
                if all(board[j][i] == char for j in range(3)): return True
            if all(board[i][i] == char for i in range(3)): return True
            if all(board[i][2 - i] == char for i in range(3)): return True
            return False
        
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)
        
        if o_count not in {x_count - 1, x_count}: # o count cannot be more and can only be x_count-1 or x_count
            return False
        if win('X') and x_count != o_count + 1: # if X wins, count of X must be o_count + 1
            return False
        if win('O') and x_count != o_count: # if O wins, count of X must be equal to count of O
            return False
        return True
from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize the 3x3 board
        board = [['' for _ in range(3)] for _ in range(3)]
        
        # Place the moves on the board
        for i, move in enumerate(moves):
            row, col = move
            if i % 2 == 0:
                board[row][col] = 'X'  # Player A
            else:
                board[row][col] = 'O'  # Player B
        
        # Function to check if a player has won
        def check_winner(player: str) -> bool:
            # Check rows and columns
            for i in range(3):
                if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
                return True
            return False
        
        # Check if player A or B has won
        if check_winner('X'):
            return "A"
        if check_winner('O'):
            return "B"
        
        # Check if the game is a draw or still pending
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
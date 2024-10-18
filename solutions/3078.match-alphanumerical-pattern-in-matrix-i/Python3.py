from typing import List

class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        # Get dimensions of board and pattern
        rows, cols = len(board), len(board[0])
        p_rows, p_cols = len(pattern), len(pattern[0])
        
        # Function to check if a part of the board matches the pattern starting at (start_row, start_col)
        def matches(start_row, start_col):
            # Maps for letters in pattern to digits in board
            letter_to_digit = {}
            digit_to_letter = {}
            
            for i in range(p_rows):
                for j in range(p_cols):
                    p_char = pattern[i][j]
                    b_digit = board[start_row + i][start_col + j]
                    
                    if p_char.isdigit():
                        if int(p_char) != b_digit:
                            return False
                    else:
                        if p_char in letter_to_digit:
                            if letter_to_digit[p_char] != b_digit:
                                return False
                        elif b_digit in digit_to_letter:
                            if digit_to_letter[b_digit] != p_char:
                                return False
                        else:
                            letter_to_digit[p_char] = b_digit
                            digit_to_letter[b_digit] = p_char

            return True
        
        # Check each possible position of the top-left corner of the pattern in the board
        for r in range(rows - p_rows + 1):
            for c in range(cols - p_cols + 1):
                if matches(r, c):
                    return [r, c]
        
        return [-1, -1]
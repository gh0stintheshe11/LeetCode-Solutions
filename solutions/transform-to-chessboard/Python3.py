from typing import List

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        def countSwaps(lines: List[int]) -> int:
            ones = sum(lines)
            n = len(lines)
            half = n // 2
            
            if n % 2 == 0:
                if ones != half: return float('inf')
                min_swaps_start_with_0 = sum(line != (i % 2) for i, line in enumerate(lines)) // 2
                min_swaps_start_with_1 = sum(line != ((i + 1) % 2) for i, line in enumerate(lines)) // 2
                return min(min_swaps_start_with_0, min_swaps_start_with_1)
            else:
                if not (ones == half or ones == half + 1): return float('inf')
                if ones == half:
                    return sum(line != (i % 2) for i, line in enumerate(lines)) // 2
                else:
                    return sum(line != ((i + 1) % 2) for i, line in enumerate(lines)) // 2
        
        n = len(board)
        
        first_row_pattern = board[0]
        second_row_pattern = [1 ^ v for v in board[0]]
        
        for i in range(n):
            if board[i] != first_row_pattern and board[i] != second_row_pattern:
                return -1

        first_col_pattern = [board[i][0] for i in range(n)]
        second_col_pattern = [1 ^ v for v in first_col_pattern]
        
        for j in range(n):
            col_j = [board[i][j] for i in range(n)]
            if col_j != first_col_pattern and col_j != second_col_pattern:
                return -1
        
        row_swaps = countSwaps(board[0])
        col_swaps = countSwaps([board[i][0] for i in range(n)])
        
        if row_swaps == float('inf') or col_swaps == float('inf'):
            return -1
        
        return row_swaps + col_swaps
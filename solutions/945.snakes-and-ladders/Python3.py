from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def get_board_value(pos):
            quot, rem = divmod(pos - 1, n)
            row = n - 1 - quot
            col = rem if (n - row) % 2 != 0 else (n - 1) - rem
            return board[row][col]
        
        n = len(board)
        target = n * n
        queue = deque([(1, 0)])  # (current_pos, move_count)
        visited = set()
        visited.add(1)
        
        while queue:
            pos, moves = queue.popleft()
            for next_pos in range(pos + 1, min(pos + 6, target) + 1):
                board_value = get_board_value(next_pos)
                if board_value != -1:
                    next_pos = board_value
                if next_pos == target:
                    return moves + 1
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
                    
        return -1
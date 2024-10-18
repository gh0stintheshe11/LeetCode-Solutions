from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])

        if z - x == 2:
            min_moves = 0
        elif z - y <= 2 or y - x <= 2:
            min_moves = 1
        else:
            min_moves = 2
        
        max_moves = (z - x - 2)

        return [min_moves, max_moves]
from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        def is_legal_direction(dR, dC):
            curR, curC = rMove + dR, cMove + dC
            found_opposite = False
            while 0 <= curR < 8 and 0 <= curC < 8:
                if board[curR][curC] == '.':
                    return False
                if board[curR][curC] == color:
                    return found_opposite
                found_opposite = True
                curR, curC = curR + dR, curC + dC
            return False

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dR, dC in directions:
            if is_legal_direction(dR, dC):
                return True

        return False
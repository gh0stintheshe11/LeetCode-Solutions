class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        moves = 0
        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1
        return moves
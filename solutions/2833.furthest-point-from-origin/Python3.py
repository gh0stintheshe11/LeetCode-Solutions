class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left_moves = moves.count('L')
        right_moves = moves.count('R')
        underscores = moves.count('_')
        # Calculate the furthest distance allowing all underscores to contribute
        return abs(left_moves - right_moves) + underscores
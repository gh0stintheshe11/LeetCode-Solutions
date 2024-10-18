class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        n = len(rooks)
        row_positions = sorted([rook[0] for rook in rooks])
        col_positions = sorted([rook[1] for rook in rooks])
        
        total_moves = 0
        
        for i in range(n):
            total_moves += abs(row_positions[i] - i)
            total_moves += abs(col_positions[i] - i)
            
        return total_moves
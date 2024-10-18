from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        
        h_pieces, v_pieces = 1, 1
        total_cost = 0
        h_idx = v_idx = 0
        
        while h_idx < len(horizontalCut) and v_idx < len(verticalCut):
            if horizontalCut[h_idx] >= verticalCut[v_idx]:
                total_cost += horizontalCut[h_idx] * v_pieces
                h_pieces += 1
                h_idx += 1
            else:
                total_cost += verticalCut[v_idx] * h_pieces
                v_pieces += 1
                v_idx += 1
                
        while h_idx < len(horizontalCut):
            total_cost += horizontalCut[h_idx] * v_pieces
            h_idx += 1
        
        while v_idx < len(verticalCut):
            total_cost += verticalCut[v_idx] * h_pieces
            v_idx += 1
        
        return total_cost